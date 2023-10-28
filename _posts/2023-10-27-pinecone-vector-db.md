---
layout: single
title: "Pinecone as a Vector DB in CML"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
date:   2023-10-27 12:00:00 +0000
categories: ml
tags: pinecone ml ai cml cloudera

---
*In this article, I demonstrate using Pinecone as a Vector DB for semantic search. To achieve this, I leverage Jupyter notebooks in CML to simplify demonstrating a production use case in its component parts.*

![](/assets/posts/2023-10-27-pinecone-vector-db/PineconeVectorDBAndCloudera.png)

## What problem does Pinecone solve for the ML architecture?

Pinecone's value proposition is in its support for a multitude of machine learning use cases. Its scalable by design-- supporting over a billion vectors and is suitable for LLM specific applications where the embedding space can be vast. It has low-latency searches which is critical for near-real time applications like what a chatbot use case would pose. Even in high-dimensional spaces, Pinecone responds quickly and efficiently. Pinecone supports hybrid search capabilities, high availability and is cost effective considering its managed architecture.

In the context of large language models specifically, I explore below how one can implement Pinecone and the sentence transformers library from Hugging Face to effectively semantic search documents from a user-posed question.

## Demo of Pinecone as a Vector DB in CML

In this Python script, I build a semantic search system for a knowledge base. I aim to convert a corpus of textual documents into vector representations, also known as embeddings, and store them into Pinecone. Once stored, I can easily retrieve the most relevant documents based on user queries.

To achieve this, I utilize the `sentence-transformers/all-mpnet-base-v2` from HuggingFace that understand the context and semantics of sentences. When a user asks a question, I convert it into a similar vector representation and then search for the most closely matching vectors (documents) within Pinecone. The end goal is to quickly and accurately fetch the most relevant document or piece of information from the knowledge base in response to the user's question.

**The entire code base presented below can be viewed in Jupyter notebooks format: https://github.com/kevinbtalbert/Pinecone-For-Semantic-Search-In-CML**


**1. Download and Install Python Libraries**

Begin with installing the pip dependencies below from PyPi. The script uses pinecone-client for vector database operations, sentence-transformers to handle sentence embeddings, and torch for tensor operations and neural network functionalities.

```python
!pip install pinecone-client==2.2.4
!pip install sentence-transformers==2.2.2
!pip install torch==2.0.1
```

**2. Import Dependencies**

Import all the necessary modules and functions from the installed libraries.

```python
import os
import pinecone
import torch
import torch.nn.functional as F
from pathlib import Path
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
```

**3. Initialize environment variables and setup Pinecone**

You will need to create an account with Pinecone at https://app.pinecone.io/?sessionType=signup if you do not already have one. From there, copy over your API key and environment (free one is `gcp-starter`). Also, since I'm declaring variables here, I am going to go ahead and declare I'll be using the sentence transformers model `all-mpnet-base-v2` from hugging face. Ultimately this will be used both for the document embeddings and question embedding. I chose the name `cml-default` as the name for the Pinecone collection (index), however you can choose your own.

```python
PINECONE_API_KEY= "insert yours here"
PINECONE_ENV = "gcp-starter"
PINECONE_INDEX = "cml-default"
EMBEDDING_MODEL_REPO = "sentence-transformers/all-mpnet-base-v2"

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
indexes = pinecone.list_indexes()

if PINECONE_INDEX not in indexes:
    pinecone.create_index(PINECONE_INDEX, dimension=768, metric="euclidean")
index_description = pinecone.describe_index(PINECONE_INDEX)
print(index_description)

collection = pinecone.Index(PINECONE_INDEX)
print("Successfully loaded " + PINECONE_INDEX)

```

**4. Load the Embeddings Model**

Load the embedding model `sentence-transformers/all-mpnet-base-v2` from Hugging Face

```python
tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL_REPO)
model = AutoModel.from_pretrained(EMBEDDING_MODEL_REPO)
```

**5. Mean Pooling Function**

This function performs mean pooling on the model's output to generate sentence embeddings, taking into consideration the attention mask for accurate averaging.

```python
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
```

**6. Embedding Generation**

This function takes in a sentence and returns its corresponding embedding. It tokenizes the input sentence, computes its embeddings using the pretrained model, and then normalizes the embeddings. Since the default model will trunate the document and only get embeddings of the first 256 tokens, we will need to ensure we pull the full document file later on before returning a response to the user.

```python
def get_embeddings(sentence):
    # Sentences we want sentence embeddings for
    sentences = [sentence]
    
    # Tokenize sentences
    encoded_input = tokenizer(sentences, padding='max_length', truncation=True, return_tensors='pt')

    # Compute token embeddings
    with torch.no_grad():
        model_output = model(**encoded_input)

    # Perform pooling
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

    # Normalize embeddings
    sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

    return (sentence_embeddings.tolist()[0])
```

**7. Inserting Embeddings into Pinecone Vector Database**

This segment reads documents from the specified directory (./data), generates embeddings for each document, and inserts the embeddings into the Pinecone vector database. I would recommend spending some time on the upsert function of pinecone. You can add several metadata attributes (I chose to include the file path) which will help you identify or process the data later on. I could imagine use cases where we identify potentially proprietary docs with a tag here, etc.

```python
## Use documents in /data directory and insert embeddings into Vector DB for each doc
def insert_embedding(pinecone_index, id_path, text):
    print("Upserting vectors...")
    vectors = list(zip([text[:512]], [get_embeddings(text)], [{"file_path": id_path}]))
    upsert_response = pinecone_index.upsert(
        vectors=vectors
        )
    print("Success")

# Create an embedding for given text/doc and insert it into Pinecone Vector DB
doc_dir = './data'
for file in Path(doc_dir).glob(f'**/*.txt'):
    with open(file, "r") as f: # Open file in read mode
        print("Generating embeddings for: %s" % file.name)
        text = f.read()
        insert_embedding(collection, os.path.abspath(file), text)
print('Finished loading Knowledge Base embeddings into Pinecone')
```

**8. Semantic Search Setup**

This final segment sets up the ability to perform semantic search on the Pinecone vector database. Given a user question, the script retrieves the most relevant response from the database and returns the source path, relevancy score, and the actual response.

```python
## Setup function to convert user question into an embedding returning most relevant response (semantic search)
def get_response_from_pinecone_vectordb(index, question):
    # Generate embedding for user question with embedding model
    retriever = SentenceTransformer(EMBEDDING_MODEL_REPO)
    xq = retriever.encode([question]).tolist()
    xc = index.query(xq, top_k=5,
                 include_metadata=True)
    
    matching_files = []
    scores = []
    for match in xc['matches']:
        # extract the 'file_path' within 'metadata'
        file_path = match['metadata']['file_path']
        # extract the individual scores for each vector
        score = match['score']
        scores.append(score)
        matching_files.append(file_path)

    response = load_context_chunk_from_data(matching_files[0])
    sources = matching_files[0]
    score = scores[0]
    return response, sources, score
  
# Return the Knowledge Base doc based on Knowledge Base ID (relative file path)
def load_context_chunk_from_data(id_path):
    with open(id_path, "r") as f: # Open file in read mode
        return f.read()
```

**9. Semantic Search!**

Create a question with relevancy to the docs in your `/docs` directory. As you can see, we are provided as a response the content from the most relevant document as well as some metadata such as the original source path of the document and its relevancy score.

```python
USER_QUESTION = "What is Iceberg" ## (replace this with your own from content in your knowledge base)
response, source, score = get_response_from_pinecone_vectordb(collection, USER_QUESTION)
print("Source Path: " + source)
print("Pinecone relevancy score: " + str(score))
print(response)
```

As you can see, the Pinecone API has a lot of capabilities. Its full capabilities are documented by Pinecone here: https://docs.pinecone.io/docs/python-client

Once again, all the code above (plus some sample text data) is consolidated in Jupyter Notebook format on my GitHub: https://github.com/kevinbtalbert/Pinecone-For-Semantic-Search-In-CML


## References and Other Resources
If any of them sound interesting to you, I would encourage you to check out the links below and get hands on. Any of the code that I have written in this article you are welcome to use and build on as you wish!

[CDP Public Cloud 60 Day Trial](https://www.cloudera.com/campaign/try-cdp-public-cloud.html)

[Fully Open Source LLM Chatbot](https://github.com/cloudera/CML_AMP_LLM_Chatbot_Augmented_with_Enterprise_Data)

[OpenAI-driven Chatbot](https://github.com/kevinbtalbert/openai-chatbot)

[Knowledge-base Building Blocks, Tools, and Scripts](https://github.com/kevinbtalbert/build_kb_tools)

[Simple OpenAI Workflow](https://raw.githubusercontent.com/kevinbtalbert/kevinbtalbert.github.io/main/assets/posts/2023-09-10-ai-workflows/simple_open_ai_implementation.py)

[SQL-driven OpenAI Workflow](https://raw.githubusercontent.com/kevinbtalbert/kevinbtalbert.github.io/main/assets/posts/2023-09-10-ai-workflows/sql_open_ai_implementation.py)