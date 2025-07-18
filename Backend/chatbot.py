from llm_config import llm
import mysql.connector

# Step 1: Generate SQL from user's natural language question
def generate_sql_from_question(question):
    prompt = f"""
You are an expert MySQL assistant for a school database.

Tables:
- students(roll_no, first_name, last_name, age, class_id, section_id, scholarship_id, bank_account_id)
- classes(class_id, class_name, section_id)
- marks(mark_id, student_roll_no, subject_id, marks_obtained)
- subjects(subject_id, subject_name)
- scholarships(scholarship_id, scholarship_name, amount)
- parents(parent_id, student_roll_no, parent_name, relation)
- bankdetails(bank_account_id, student_roll_no, bank_name, account_number, ifsc_code)

Rules:
- Use only proper SQL syntax.
- Return only the SQL query.
- Use JOINs where needed.
- Don't explain anything.
- Examples: "Grade 10" → class_name='Grade 10'; "Math" → subject_name='Mathematics'

User Question:
\"\"\"{question}\"\"\"
"""
    response = llm.predict(prompt)
    sql = response.replace("```", "").replace("sql", "").strip()
    return sql

# Step 2: Run SQL query on the MySQL database
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
        result = "\n".join([", ".join(map(str, row)) for row in rows])
        return f"📊 {', '.join(columns)}\n{result}"
    except Exception as e:
        return f"❌ SQL Error: {e}"

# Step 3: Chat loop
if __name__ == "__main__":
    print("💬 Ask a question from your school database (type 'exit' to quit)\n")
    while True:
        user_input = input("👨‍🎓 You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Exiting chatbot...")
            break

        sql = generate_sql_from_question(user_input)
        print(f"\n📄 Generated SQL:\n{sql}")
        answer = run_sql_query(sql)
        print(f"\n🤖 Chatbot Answer:\n{answer}\n")
