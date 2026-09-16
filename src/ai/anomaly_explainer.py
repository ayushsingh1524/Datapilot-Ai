import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def explain_anomalies(anomalies: list) -> str:
    prompt = f"""
You are a data analyst.

Analyze these unusual orders:

{json.dumps(anomalies, default=str)}

Explain:
- How many unusual orders were found
- Which products/orders are unusual
- Why they may be considered unusual based on their order amount

Rules:
- Be concise.
- Do not invent information.
- Use ₹ for monetary values.
- Do not use Markdown.
- Do not use **, *, #, or bullet points.
- Write 2-3 short plain-text sentences.
- Keep the explanation under 100 words.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )

    return response.text.strip()