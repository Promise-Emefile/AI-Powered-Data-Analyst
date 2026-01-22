from ai.llm_cilent import call_llm

def generate_sql(question, schema):
    schema_text = "\n".join(
        f"{t}: {', '.join(cols)}" for t, cols in schema.items()
    )
    prompt = f"""
You are a SQL expert.
Only generate SELECT queries.
Limit results to 100 rows.

Schema:
{schema_text}

Question: {question}
SQL:
"""
    return call_llm(prompt).strip()