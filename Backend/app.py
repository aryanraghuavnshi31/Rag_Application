import streamlit as st
from llm_config import llm
import mysql.connector

st.set_page_config(page_title="School Chatbot", layout="centered")
st.title("🏫 School Chatbot (LangChain + SQL + OpenRouter)")

# Input from user
user_question = st.text_input("Ask a question about the school database:")

def generate_sql(question):
    prompt = f"""
You are an expert SQL assistant for a school database.

Tables:
- students(roll_no, first_name, last_name, age, class_id, section_id, scholarship_id, bank_account_id)
- classes(class_id, class_name, section_id)
- marks(mark_id, student_roll_no, subject_id, marks_obtained)
- subjects(subject_id, subject_name)
- scholarships(scholarship_id, scholarship_name, amount)
- parents(parent_id, student_roll_no, parent_name, relation)
- bankdetails(bank_account_id, student_roll_no, bank_name, account_number, ifsc_code)

Rules:
- Use only MySQL syntax.
- Use JOINs where necessary.
- Don't explain anything.
- Just return a valid SQL query based on:
\"\"\"{question}\"\"\"
"""
    response = llm.predict(prompt)
    return response.replace("```", "").replace("sql", "").strip()

def run_sql_query(sql):
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Aryan1331@#",
            database="school_db",
            auth_plugin="mysql_native_password"
        )
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()

        if not rows:
            return "⚠️ No data found."
        result = [dict(zip(columns, row)) for row in rows]
        return result
    except Exception as e:
        return f"❌ SQL Error: {e}"

if user_question:
    with st.spinner("Thinking..."):
        sql_query = generate_sql(user_question)
        st.code(sql_query, language="sql")
        result = run_sql_query(sql_query)

        if isinstance(result, str):
            st.error(result)
        else:
            st.success("✅ Query executed successfully!")
            st.dataframe(result)
