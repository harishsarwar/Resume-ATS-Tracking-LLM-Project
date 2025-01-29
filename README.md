# Smart ATS

## Overview
Smart ATS is a Streamlit-based web application that helps job seekers improve their resumes by evaluating them against a given job description. It leverages LLM capabilities using Groq's `ChatGroq` model to provide an ATS-friendly score, missing keywords, and a profile summary.

## Features
- Upload a resume (PDF format).
- Analyze the resume against a provided job description.
- Get a JD match percentage, missing keywords, and a profile summary.
- User-friendly interface with Streamlit.

## Requirements
- Python 3.12.4
- Streamlit
- PyPDF2
- langchain_groq
- dotenv


## Usage
Run the application with:
```sh
streamlit run app.py
```

## How It Works
1. Paste the job description.
2. Upload your resume (PDF).
3. Click "Submit" to get insights.



