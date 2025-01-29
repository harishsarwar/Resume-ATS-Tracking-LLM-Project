import streamlit as st
import PyPDF2 as pdf
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("API_KEY")
os.environ["API_KEY"] = api_key

# Function to Intract with model.

def get_gorq_respponse(input):
    model = ChatGroq(api_key = api_key,
                     model_name="Llama3-8b-8192")
    response = model.invoke(input)
    return response


# Reading pdf

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
        return text
    

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""


## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gorq_respponse(input_prompt)
        st.subheader(response)