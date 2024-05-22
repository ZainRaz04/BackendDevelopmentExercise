# utils.py
import pandas as pd
from langchain import LLMChain, OpenAI, PromptTemplate

def read_sales_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.json'):
        return pd.read_json(file)
    elif file.name.endswith('.xlsx'):
        return pd.read_excel(file, engine='openpyxl')
    elif file.name.endswith('.xls'):
        return pd.read_excel(file, engine='xlrd')
    else:
        raise ValueError("Unsupported file format")


import openai

openai.api_key = 'sk-proj-MoqzAgRFddG3wdDLNwsQT3BlbkFJdBpma2G9eBpGfNo8xtc5'

def generate_insights(df, question):

    
    template = """You are a data analyst with access to the following dataset:
    {data}

    Based on the above data, please answer the following question:
    Question: {question}
    Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["data", "question"])

    
    llm = OpenAI(model_name="text-davinci-003")

    
    chain = LLMChain(llm=llm, prompt=prompt)

    def answer_question(df, question):
        
        data_str = df.to_string()
       
        answer = chain.run(data=data_str, question=question)
        return answer

      
    answer = answer_question(df, question)
    print("Answer:", answer)
    return answer
