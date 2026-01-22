import re
import pandas as pd
import streamlit as st

def clean_sql(sql: str) -> str:
    sql = re.sub(r"'''sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"'''", "", sql)
    return sql.strip()

def run_query(sql, engine):
    try:
        return pd.read_sql(sql, engine)
    except Exception as e:
        st.error(str(e))
        raise
