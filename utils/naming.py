import re

def clean_table_name(name: str) -> str:
    """Cleans the table name by removing special characters and converting to lowercase."""
    name = name.lower()
    name = re.sub(r'\W+', '_', name)
    return name