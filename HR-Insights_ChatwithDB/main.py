from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from PIL import Image


# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function To retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEE and has the following columns - 
    ID, NAME, AGE, DEPARTMENT, SALARY, PERFORMANCE_SCORE, YEARS_OF_EXPERIENCE, 
    LAST_PROMOTION_YEAR, LOCATION \n\nFor example,\nExample 1 - How many entries 
    of records are present?, the SQL command will be something like this 
    SELECT COUNT(*) FROM EMPLOYEE;
    \nExample 2 - Tell me all the employees in the IT department?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    WHERE DEPARTMENT="IT"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit App
st.set_page_config(page_title="AI-Driven HR Insights", page_icon=":bar_chart:", layout="wide")

# Apply custom CSS for colors
st.markdown("""
    <style>
        .main {
            background-color: #F3F2F1;
        }
        h1 {
            color: #E71D73; /* TCS Pink */
        }
        .stButton button {
            background-color: #1E91D6; /* TCS Blue */
            color: white;
        }
        .stTextInput > div > div > input {
            background-color: #FFE9F3; /* Light Pink */
            color: #1E91D6; /* TCS Blue */
        }
    </style>
    """, unsafe_allow_html=True)
st.title("AI-Driven HR Insights")
st.markdown("""
### Welcome to the AI-Driven HR Insights Dashboard!

This Proof of Concept (POC) showcases the integration of AI in the HR industry, providing a smart interface to query employee data using natural language. Simply ask a question about the employee database, and our AI-powered system will convert it to an SQL query, fetch the data, and present it to you.

**Features:**
- Query employee data using natural language.
- AI-powered conversion of questions to SQL queries.
- Real-time data retrieval from the employee database.
- Easy-to-use interface designed for HR professionals.

**Use Cases:**
- Retrieve employee performance scores.
- Find employees based on department, location, and other criteria.
- Analyze salary distributions and other key metrics.
""")

# Input section
question = st.text_input("Ask your question about employee data:", key="input", placeholder="e.g., How many employees are in the IT department?")

submit = st.button("Get Insights")

# if submit is clicked
if submit:
    with st.spinner("Processing your request..."):
        response = get_gemini_response(question, prompt)
        st.subheader("Generated SQL Query")
        st.code(response)
        data = read_sql_query(response, "employee_kpi.db")
        
        if data:
            st.subheader("Query Results")
            st.dataframe(data)
        else:
            st.warning("No data found for the given query.")

st.sidebar.header("About")
st.sidebar.info("""
This application is a demonstration of how AI can be leveraged in the HR industry to streamline data retrieval and analysis. It uses Google Gemini for natural language processing and an SQLite database for storing employee data.

**Developed by:** Yash Kavaiya
**Contact:** [LinkedIn](https://www.linkedin.com/in/yashkavaiya/)
""")

# Footer
st.markdown("""
---
**Note:** This is a POC and not intended for production use. Data privacy and security are paramount; ensure compliance with relevant regulations when handling real employee data.
""")
