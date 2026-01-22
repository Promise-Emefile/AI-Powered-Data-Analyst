import pandas as pd

def run_query(sql, engine):
    try:
        return pd.read_sql(sql, engine)
    except Exception as e:
        st.error(str(e))
        raise
