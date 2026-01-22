from ai.llm_cilent import call_llm

def generate_insights(df):
    preview = df.head(10).to_csv(index=False)

    prompt = f"""
Here is a dataset result:
{preview}

Give:
1. Key insights
2. Business implications
3. Suggested follow-up questions
"""
    return call_llm(prompt).strip()