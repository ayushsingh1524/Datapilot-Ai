import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_sql(question: str, schema: str) -> str:
    """
    Generate a PostgreSQL SELECT query using
    relevant knowledge retrieved through RAG.
    """

    prompt = f"""
You are an expert PostgreSQL data analyst.

You are using a Retrieval-Augmented Generation (RAG) system.

The following information was retrieved from the
database knowledge base:

--- RAG CONTEXT ---
{schema}
--- END RAG CONTEXT ---

User question:
{question}

Generate a PostgreSQL SQL query that answers
the user's question.

Rules:
- Return only SQL.
- Use only SELECT statements.
- Do not modify the database.
- Use only tables and columns supported by the RAG context.
- Follow the business rules in the RAG context.
- Use total_amount for revenue calculations.
- Do not invent tables or columns.
- Make sure the SQL is valid PostgreSQL.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text.strip()