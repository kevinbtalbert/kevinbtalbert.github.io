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