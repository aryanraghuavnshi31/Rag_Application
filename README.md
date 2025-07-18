🧠 Project Overview
-
This project is a School Chatbot built using a Retrieval-Augmented Generation (RAG) approach.
It combines LangChain, OpenRouter (GPT-3.5), and a MySQL database to allow users to ask natural language questions and get live answers from structured school data.

The chatbot runs inside a clean, interactive Streamlit web UI, making it suitable for real-world usage or academic submission.


-----------------------------------------------

🎯 Project Objective
--
Convert natural language questions (e.g., “Who got the Merit Scholarship?”)

Into valid SQL queries using LLM

Run those queries on a real MySQL school_db

 Display the results instantly on the web interface

This simulates how modern LLMs can be used to query real-world structured data.

----------------------------

🔍 Key Features
--

✅ Natural language to SQL query generation
    
✅ Live connection to MySQL school database

 
 ✅ Web-based interface using Streamlit


 ✅ Secure .env file for API key management

    

✅ Queries across students, marks, subjects, classes, parents, and scholarship


    
🧰 Technologies Used
--
| Component    | Tech Used                  |
| ------------ | -------------------------- |
| Language     | Python                     |
| LLM Backend  | OpenRouter (GPT-3.5 Turbo) |
| Framework    | LangChain                  |
| UI           | Streamlit                  |
| Database     | MySQL (`school_db`)        |
| Env Handling | python-dotenv              |


----------------

📁 Project Structure
-

school_chatbot_final/
│
├── .env     

├── app.py       

├── llm_config.py  

├── chatbot.py 

├── connect_mysql.py 

├── requirements.txt 

├── README.md     

├── school_db.sql   

└── venv/                 


---

⚙️ Installation & Setup Guide
-

Follow these steps to install and run the School Chatbot application:-

✅ 1. Clone or Download the Project
-
git clone https://github.com/your-username/school_chatbot_final.git
cd school_chatbot_final

Or just download the ZIP and extract it.

✅ 2. Create a Virtual Environment
-
python -m venv venv

✅ 3. Install Required Dependencies
-
pip install langchain langchain-openai python-dotenv mysql-connector-python streamlit

✅ 4. Set Up .env File
-
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

✅ 5. Set Up MySQL Database
-
CREATE DATABASE school_db;
-- Then run the provided SQL dump to create tables and insert data

Update your DB credentials in app.py or chatbot.py if needed:

user="root",
password="your_password",
host="127.0.0.1",
database="school_db"

✅ 6. Run the Chatbot (Web UI)
-
streamlit run app.py
Opens in browser at: http://localhost:8501

screenshots:-
-

<img width="1365" height="651" alt="image" src="https://github.com/user-attachments/assets/f3319268-39cd-4438-85ae-b23a85eac256" />


<img width="1360" height="720" alt="image" src="https://github.com/user-attachments/assets/8e48de96-6053-41a2-b28b-c335a4b03606" />


Project vedio:-
-
https://drive.google.com/file/d/1kOlLdHoRa-kM29e9mHh4Ex4_cnsTuj1z/view?usp=drive_link

    
