---
layout: single
title: "Demo: CDF, CML, and OpenAI for Custom Chatbots"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
date:   2023-09-28 12:00:00 +0000
categories: ml
tags: nifi openai data cml ai cloudera

---
*This video demonstrates how Cloudera DataFlow (CDF), Cloudera Machine Learning (CML), and OpenAI can be leveraged to build a custom knowledge base that an enterprise can use for enabling individuals to access their own Custom Q and A chatbot. Using CDF, we deploy a Nifi template that accepts a website’s sitemap as parameter of a POST request made from Postman, and outputs the important html content of every page from the website. CML utilizes OpenAI's API to semantic search with the gathered documents and outputs a result based on content from the custom knowledge base.*

<div class="embed-container">
    <iframe width="640" height="390" 
    src="https://github.com/kevinbtalbert/kevinbtalbert.github.io/raw/main/assets/posts/2023-09-28-custom-kb-demo.md/NiFi%20%2B%20OpenAI%20LLM%20Demo%20w%20Kevin.mp4" 
    frameborder="0" allowfullscreen></iframe>
</div>
<style>
.embed-container {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  overflow: hidden;
  max-width: 100%;
}
.embed-container iframe,
.embed-container object,
.embed-container embed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>



## Want to Read More and Get Started?
The capabilities here are incredible, and I hope you'll take some time to play around with these use cases. If any of them sound interesting to you, I would encourage you to check out the links below and get hands on. Any of the code that I have written in this article you are welcome to use and build on as you wish!

[CDP Public Cloud 60 Day Trial](https://www.cloudera.com/campaign/try-cdp-public-cloud.html)

[Fully Open Source LLM Chatbot](https://github.com/cloudera/CML_AMP_LLM_Chatbot_Augmented_with_Enterprise_Data)

[OpenAI-driven Chatbot](https://github.com/kevinbtalbert/openai-chatbot)

[Knowledge-base Building Blocks, Tools, and Scripts](https://github.com/kevinbtalbert/build_kb_tools)

[Simple OpenAI Workflow](https://raw.githubusercontent.com/kevinbtalbert/kevinbtalbert.github.io/main/assets/posts/2023-09-10-ai-workflows/simple_open_ai_implementation.py)

[SQL-driven OpenAI Workflow](https://raw.githubusercontent.com/kevinbtalbert/kevinbtalbert.github.io/main/assets/posts/2023-09-10-ai-workflows/sql_open_ai_implementation.py)