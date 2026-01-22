import pandas as pd

def run_query(sql, engine):
    df = pd.read_sql(sql, engine)
    return df