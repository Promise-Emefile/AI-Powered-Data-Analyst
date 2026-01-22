import pandas as pd
from utils.naming import clean_table_name

def ingest_csv(file, engine):
    """Ingests a CSV file into the database."""
    df = pd.read_csv(file)
    table_name = clean_table_name(file.name.split(".")[0])
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    return table_name