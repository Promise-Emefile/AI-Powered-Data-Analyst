import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o"),
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
        temperature=0.7
    )
    try:
        return response.choices[0].message.content
    except Exception:
        return str(response)
