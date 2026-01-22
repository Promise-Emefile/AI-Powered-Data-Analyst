# AI-Powered Data Analyst 🚀
#### Democratizing data analysis with the power of AI.
#### This tool bridges the gap between business users and complex datasets by converting natural language questions into executable SQL queries. Simply upload a CSV file, ask questions in plain English, and get instant insights — no coding required!

## ✨ Features
### Natural Language Processing  
#### Leverages OpenAI’s GPT models to transform everyday questions into precise SQL queries.

### Safety First  
#### Built-in validation ensures only safe SELECT operations are executed.
### Interactive Experience  
#### Streamlit-powered web interface with automatic visualizations for query results.
### AI-Driven Insights  
#### Generates business implications and follow-up questions from query outputs.

## 🛠️ Tech Stack
#### Python — core language
#### Streamlit — interactive web app framework
#### SQLAlchemy + SQLite — database management
#### Pandas — data processing
#### OpenAI GPT-4 — natural language to SQL conversion

## 🚀 Getting Started
### 1. Clone the repository
##### git clone https://github.com/Promise-Emefile/AI-Powered-Data-Analyst.git
##### cd AI-Powered-Data-Analyst

## Install dependencies
##### pip install -r requirements.txt

## Set up your API key
##### Create a .env file in the project root:
##### OPENAI_API_KEY="your_openai_api_key_here"

## Run the app
##### streamlit run app.py

## 📊 Usage
#### Upload a CSV file.
#### Ask questions in plain English (e.g., “Show me fraud cases that happened on weekdays”).

#### Get instant SQL queries, results, and visualizations.

#### Explore AI-generated insights and suggested follow-up questions.

## 🔒 Security Notes
#### Only SELECT queries are allowed — destructive operations (DROP, DELETE, etc.) are blocked.

#### API keys should be stored securely in .env or Streamlit Cloud secrets.

#### .env is included in .gitignore to prevent accidental leaks.

## 🌟 Potential Applications
#### Quick data exploration

#### Rapid prototyping of analytics dashboards

#### Empowering non-technical business users to query data

#### Teaching SQL concepts through natural language

## 🤝 Contributing
#### Contributions are welcome!

#### Fork the repo

#### Create a feature branch

#### Submit a pull request

## 
### Promise Emefile
### Data Analyst and AI Engineer
### promiseemefile@gmail.com
