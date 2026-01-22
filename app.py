import streamlit as st
import os
import atexit

from db.session_db import create_session_engine
from db.ingest import ingest_csv
from db.query import run_query
from utils.schema_utils import extract_schema
from utils.sql_safety import is_sql_safe
from ai.sql_generator import generate_sql
from ai.insight_generator import generate_insights

st.set_page_config(page_title="AI Data Analyst", layout="wide")


#Session DB
if 'engine' not in st.session_state:
    engine, db_path = create_session_engine()
    st.session_state.engine = engine
    st.session_state.db_path = db_path

def cleanup():
    try:
        os.remove(st.session_state.db_path)
    except:
        pass

atexit.register(cleanup)

st.title("AI-Powered Data Analyst")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    table = ingest_csv(uploaded_file, st.session_state.engine)
    st.success(f"Loaded table: {table}")

    # Display schema
    schema = extract_schema(st.session_state.engine)
    st.session_state.schema = schema

    question = st.text_input("Enter your data question:")

    if question and "schema" in st.session_state:
        sql = generate_sql(question, st.session_state.schema)
        st.subheader("Generated SQL Query")
        st.code(sql, language="sql")

        if is_sql_safe(sql):
            df = run_query(sql, st.session_state.engine)
            st.subheader("Query Results")
            st.dataframe(df)

            if df.shape[1] == 2:
                st.bar_chart(df.set_index(df.columns[0]))
                
                insight = generate_insights(df)
                st.subheader("AI-Generated Insight")
                st.markdown("### insight")
                st.write(insight)
        else:
            st.error("Unsafe SQL detected. Please modify your question.")
                