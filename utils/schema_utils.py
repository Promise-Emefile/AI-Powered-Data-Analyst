from sqlalchemy import inspect

def extract_schema(engine):
    inspector = inspect(engine)
    schema = {}

    for table in inspector.get_table_names():
        cols = inspector.get_columns(table)
        schema[table] = [c['name'] for c in cols]
    return schema