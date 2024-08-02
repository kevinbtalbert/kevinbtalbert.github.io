---
layout: single
title: "Document Analysis with Cohere CommandR and FAISS"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
date:   2024-08-02 12:00:00 +0000
categories: ml
tags: cohere faiss ml ai cml cloudera

---
## Document Analysis with Cohere CommandR and FAISS

These past several weeks I got the chance to write the integration Applied Machine Learning Prototype ("AMP") for Cohere and Cloudera which was added to our official AMP catalog yesterday. The use case it drives is document intelligence for PDFs with reference pointers back to the source snippet. What this means to the end user is that they can see exactly what source(s) the answer was generated from lending to more verifiable AI.

Cohere's Command R LLM is a cutting-edge AI language model that excels in natural language processing tasks, capable of generating coherent (no pun intended!) and contextually relevant text based on input prompts. The AMP also introduces another vector store to the platform with Facebook's FAISS, short for Facebook AI Similarity Search, an open-source library built for similarity search and clustering of dense vectors. 

This AMP combines the best of both Cohere and Cloudera, automatically deploying an application, loading vectors into FAISS, and interfacing with Cohere's Command R LLM within the Cloudera Machine Learning service. The goal is to also release a dedicated runtime soon which adds the full Cohere Toolkit capability OOTB to CML for AI developers to build robust production-grade applications on Cohere's models.

Check out the project [here](https://github.com/cloudera/CML_AMP-Document-Analysis-with-Cohere-CommandR-and-FAISS) or deploy it directly from the CML AMP Catalog.

### Architecture

![](/assets/posts/2024-08-02-cohere-integration/cohere-architecture.jpg)

### Whats it look like?!

![](/assets/posts/2024-08-02-cohere-integration/chatbot.png)


## References and Other Resources

[Document Analysis with Cohere CommandR and FAISS](https://github.com/cloudera/CML_AMP-Document-Analysis-with-Cohere-CommandR-and-FAISS)

[CDP Public Cloud 60 Day Trial](https://www.cloudera.com/campaign/try-cdp-public-cloud.html)