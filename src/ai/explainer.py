import os
import json

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def explain_results(question: str, results: list) -> str:

    prompt = f"""
You are a data analyst.

Explain the following database results in simple, concise language.

User question:
{question}

Query results:
{json.dumps(results, default=str)}

Rules:
- Give a direct answer to the user's question.
- Mention the most important numbers.
- Highlight useful patterns or comparisons.
- Do not invent information.
- Use ₹ for monetary values.
- Never use $ unless the data explicitly uses US dollars.
- Keep the explanation under 100 words.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )

    return response.text.strip()