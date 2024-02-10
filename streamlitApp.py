import os 
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
# from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQgenerator import generate_evaluate_chain
from langchain_community.callbacks import get_openai_callback
from src.mcqgenerator.logger import logging


#load Json file
with open(r"C:\Users\Admin\MCQ_generator_Using_Langchain_and_OpenAI\Response.json",'r') as file:
    RESPONSE_JSON= json.load(file)

#Creating title for the app
st.title("MCQs creator Application with Langchain")

#Create a form using st.form
with st.form("user inputs"):
    #File upload
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    #input field
    mcq_count= st.number_input("No. of MCQs", min_value=3,max_value=50)
    
    #subject
    subject= st.text_input("Insert Subject",max_chars=20)

    #Quiz Tone
    tone = st.text_input("Complexity level of quetions", max_chars=20,placeholder="Simple")
     
    button = st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject":subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                raise Exception("Not getting MCQs")
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost(in doller):{cb.total_cost}")

                if isinstance(response,dict):
                    quiz =response.get("quiz",None)
                    if quiz is not None:
                        table_data = get_table_data(quiz=quiz)
                        if table_data is not None:
                            df =pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            #display the review in a text box as well 
                            
                            df.to_csv("machinelearning.csv",index=False)

                        else:
                            st.error("Error in the table data")
                else:
                    st.write(response)
