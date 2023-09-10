---
layout: single
title: "Leveraging OpenAI for your Workflows"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
date:   2023-09-10 12:00:00 +0000
categories: ml
tags: openai data cml ai cloudera

---
*The article discusses the rising importance of AI in modernizing business workflows across various sectors, including finance and government. It specifically focuses on use cases for adopting AI through tools like Cloudera's CML platform to offer valuable insights quickly and at a low cost. The article provides Python code samples for these applications, emphasizing how easy it is to set up OpenAI API with just a few lines of code.*

![](/assets/posts/2023-09-10-ai-workflows/cover.png)

The hot button topic in the industry right now is how businesses and organizations can leverage AI to modernize their workflows. Because of how expansive this has become over the last year, the capabilities of this technology have really managed to touch almost every aspect of the big data industry. I have read several articles this past week of financial services companies and government organizations I never thought would be early adopters of AI, modernizing their internal processes. With everything from HR departments screening job descriptions against resumes, to customer service departments analyzing a customer's sentiments to decide options, to IT divisions automating code reviews, there is massive untapped potential that your organization should be doing to stay ahead of the curve. 

As is the theme with this blog, I am all about providing easy solutions that you can jump into using with little prework. So oftentimes the path to building something great seems to revolve around spending 50% of your time just getting your environments and technology set up to start building. In the AI space, much of the insights companies want to get out of AI can begin with a common baseline that is deployable across solutions. This is what Cloudera has provided with AMPs (Applied Machine Learning Prototypes) in its CML offering. This past week, I've been working to enable GPT 3.5 and GPT 4 as the semantic search engine for the fully open-source [LLM Chatbot Augmented with Enterprise Data](https://github.com/cloudera/CML_AMP_LLM_Chatbot_Augmented_with_Enterprise_Data). The idea is that because of the massive amount of parameters GPT 3.5 and GPT 4 have been trained on (some estimates are in the trillions), they provide an incredibly accurate answer to the prompt/context they are given (much more accurate than any open source counterpart, to date). If you want to follow my efforts on this, check out that repo here: [OpenAI Chatbot Leveraging GPT 3.5 and GPT 4](https://github.com/kevinbtalbert/openai-chatbot).

## Use Case: Internal Knowledge Base

For my own part, this AMP was bourne out of the notion that we need an internal knowledge base with context of data scraped after September 2021, which is the latest set of data OpenAI's ChatGPT provides. Building an internal knowledge base may be driven by many factors, but for me the first (and most obvious) source would be our public documentation. All the current pages on a website can typically be associated with a sitemap xml file. Using the tools I wrote [here (Scripts/Utilities to Build a Knowledge Base)](https://github.com/kevinbtalbert/build_kb_tools), you can build your internal knowledge base from a sitemap and use the created files to power your internal knowledge base app with some tweaking to the [OpenAI Chatbot Leveraging GPT 3.5 and GPT 4](https://github.com/kevinbtalbert/openai-chatbot) project. 

In general, this is the architectural idea behind an implementation of this concept:

![](/assets/posts/2023-09-10-ai-workflows/ex_architecture1.png)
[*View Larger*](/assets/posts/2023-09-10-ai-workflows/ex_architecture1.png)

*1 - https://github.com/kevinbtalbert/openai-chatbot*

*2/3 - https://github.com/kevinbtalbert/build_kb_tools*

*6 - https://platform.openai.com/account/api-keys*


## Extending OpenAI API Use Cases

Even though the internal knowledge base is a great use case, there are several other engines available more fine tuned to specific tasks. Like the example earlier I provided around code checking, OpenAI provides a fine-tuned engine for code verification/creation/completion as well. OpenAI has created an API for users to take advantage of their semantic search engine (and also one for training) that can literally be setup in less than 100 lines of code. I think the cool thing about adopting this API into your workflow is that you can amortize its benefits to so many more use cases than just a chatbot. Effectively anywhere you can access the internet, you can leverage the OpenAI python library to transmit/receive insights from your data. You can check out their PyPi library, and install it via pip: [openai 0.28.0](https://pypi.org/project/openai/).

To get you started, consider the following starter code I wrote which can be extended to more broadly support complex use cases. Note that to access the OpenAI API, you will need to create an OpenAI key: https://platform.openai.com/account/api-keys

```python 
#shell: !pip install openai
import openai

openai.api_key = "sh-xxxx"

def get_response(question, context, engine):

    enhanced_question = """Answer this question based on given context. If the context is insufficient to answer the question, rely on your own knowledge base. """ + question
    
    response = openai.ChatCompletion.create(
        model=engine,
        messages=[
            {"role": "system", "content": str(context)},
            {"role": "user", "content": str(enhanced_question)}
            ]
    )
    
    return response['choices'][0]['message']['content']

def main():
    question = "What are AMPs?"
    context = """AMPs are ML projects that can be deployed with one click directly from Cloudera Machine Learning (CML). AMPs enable data scientists to go from an idea to a fully working ML use case in a fraction of the time. It provides an end-to-end framework for building, deploying, and monitoring business-ready ML applications instantly. 1. Prototypes encode best practices for solving machine problems. 2. Each step in the solution (e.g. data ingest, model training, model serving etc.) is declared in a yaml configuration file. 3. Run examples locally or automatically deploy steps within your configuration file using Cloudera Machine Learning."""
    engine_options = ['gpt-3.5-turbo', 'gpt-4']

    ## Response with GPT 3.5
    print(get_response(question, context, engine_options[0]))

    ## Response with GPT 4
    print(get_response(question, context, engine_options[1]))

if __name__ == "__main__":
    main()

```

[Full Code of this simple OpenAI Implementation here](https://raw.githubusercontent.com/kevinbtalbert/kevinbtalbert.github.io/main/assets/posts/2023-09-10-ai-workflows/simple_open_ai_implementation.py)

While this example is very simple, it demonstrates the API's capabilities to drive meaningful insights quickly, easily, and with very minimal cost to your organization. Most queries will cost less than a cent to run and are very accurate against the provided context. If you take advantage of the AMPs I mentioned previously, CML takes care of vectorizing your "context" that you provide in the form of text files, picking the file closest to your query as context to send to OpenAI's semantic search API.

## Use Case: Code Explainability

Perhaps even cooler is the [Codex model series](https://platform.openai.com/docs/guides/code), provided by OpenAI which could enable you to bring data analyst insights to non-technical users: [Codex Model Overview](https://platform.openai.com/docs/models/codex). As an example of this use case, since users of the CML platform already have their data stored in Cloudera's Data Platform, they can call `DESCRIBE <table>;` on one of the tables in their database and feed this as context to the OpenAI model, asking it to generate a SQL query to run for more advanced insights in CDW (Cloudera Data Warehouse). These connections are very simple to make and the UI provides [sample code](/assets/posts/2023-09-10-ai-workflows/sample_code.png) for you to build from. The capabilities are really endless here, and with the inbuilt connections that CML provides, you could have this use case up and running in under an hour. You can ask questions of your dataset and have the engine build a SQL query that answers it. You can even feed the answer directly back into your SQL engine. 

In general, this is the architecture you are implementing; however, you would likely adapt this to include some kind of UI (like Gradio, Flask, Nginx, etc.) to do this at scale. I could also see this being done as a layer to form visualizations from their SQL core.

![](/assets/posts/2023-09-10-ai-workflows/ex_architecture2.png)
[*View Larger*](/assets/posts/2023-09-10-ai-workflows/ex_architecture2.png)

Check out the example implementation of this below:

```python
#shell: !pip install openai
import openai
import cml.data_v1 as cmldata

openai.api_key = "sh-xxxx"

def get_cdw_table_schema(database, table_name):
    CONNECTION_NAME = "default-impala"
    conn = cmldata.get_connection(CONNECTION_NAME)
    SQL_QUERY = "DESCIBE " + "`" + str(database) + "`." + str(table_name) + "; "
    dataframe = conn.get_pandas_dataframe(SQL_QUERY)
    return dataframe.to_string()

def run_sql(sql):
    dataframe = conn.get_pandas_dataframe(sql)
    return dataframe.to_string()

def get_response(question, context, engine):

    enhanced_question = """Build a SQL query to solve the given question based on given table structure. """ + question
    
    response = openai.ChatCompletion.create(
        model=engine,
        messages=[
            {"role": "system", "content": str(context)},
            {"role": "user", "content": str(enhanced_question)}
            ]
    )
    
    return response['choices'][0]['message']['content']

def main():
    question = "How many people are attending university X?"
    context = get_cdw_table_schema("database-name-here", "table-name-here")
    engine_options = ['gpt-3.5-turbo', 'gpt-4']
    
    ## Response with GPT 3.5
    res1 = get_response(question, context, engine_options[0])
    print(res1)
    ## You may have to strip out some text the LLM provides back to get the raw SQL but ideally...
    print(run_sql(res1))

    ## Response with GPT 4
    res2 = get_response(question, context, engine_options[1])
    print(run_sql(res2))
    

if __name__ == "__main__":
    main()

```

[Full Code of this SQL OpenAI Implementation here](https://raw.githubusercontent.com/kevinbtalbert/kevinbtalbert.github.io/main/assets/posts/2023-09-10-ai-workflows/sql_open_ai_implementation.py)


## Want to Read More and Get Started?
The capabilities here are incredible, and I hope you'll take some time to play around with these use cases. If any of them sound interesting to you, I would encourage you to check out the links below and get hands on. Any of the code that I have written in this article you are welcome to use and build on as you wish!

[CDP Public Cloud 60 Day Trial](https://www.cloudera.com/campaign/try-cdp-public-cloud.html)

[Fully Open Source LLM Chatbot](https://github.com/cloudera/CML_AMP_LLM_Chatbot_Augmented_with_Enterprise_Data)

[OpenAI-driven Chatbot](https://github.com/kevinbtalbert/openai-chatbot)

[Knowledge-base Building Blocks, Tools, and Scripts](https://github.com/kevinbtalbert/build_kb_tools)

[Simple OpenAI Workflow](https://raw.githubusercontent.com/kevinbtalbert/kevinbtalbert.github.io/main/assets/posts/2023-09-10-ai-workflows/simple_open_ai_implementation.py)

[SQL-driven OpenAI Workflow](https://raw.githubusercontent.com/kevinbtalbert/kevinbtalbert.github.io/main/assets/posts/2023-09-10-ai-workflows/sql_open_ai_implementation.py)