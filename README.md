## Project Description

This project is a natural language interface for interacting with SQL databases. It allows users to ask questions in plain English and get answers directly from a database. The system uses LangChain to convert natural language queries into SQL commands, which are then executed against either a local SQLite database (`student.db`) or a remote MySQL database.

The interface is built using Streamlit, enabling an interactive chat-like experience where users can input their queries and receive responses in real time. This setup is particularly useful for non-technical users who want to explore or analyze data without writing SQL queries manually.

---

## Process Overview

1. **User Input**: The user selects the database type (SQLite or MySQL) and provides credentials or uses the local `student.db`.
2. **API Key Entry**: The user inputs their OpenAI API key to enable natural language processing.
3. **Language Model Interaction**: LangChain, in conjunction with OpenAI's GPT model, processes the user's query and converts it into a valid SQL command.
4. **SQL Execution**: The generated SQL query is executed on the selected database using SQLAlchemy.
5. **Results Display**: The results of the query are displayed in the chat interface for the user to review.

---

## Tools and Technologies Used

- **Python**: Core programming language used for building the application.
- **Streamlit**: Framework for creating the interactive web application.
- **LangChain**: Framework to interface with language models and generate SQL queries from natural language.
- **OpenAI GPT (via LangChain)**: Language model used for interpreting and generating queries.
- **SQLite3**: Local database used for demo/testing (`student.db`).
- **MySQL**: External database support for real-world integration.
- **SQLAlchemy**: ORM and database toolkit for managing SQL connections and query execution.
- **ChatOpenAI & create_sql_agent**: LangChain modules used for creating the agent that handles query translation and execution.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DevaPriya5102/ChatSQL.git
   cd ChatSQL

   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

In the sidebar:
- Choose between SQLite (`student.db`) or connect to your own MySQL database
- Enter your OpenAI API key
- Start chatting with your database using natural language queries

