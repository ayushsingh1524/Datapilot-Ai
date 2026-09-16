from sqlalchemy import text

from src.ai.embeddings import generate_embedding
from src.database.connection import get_engine


def store_schema_embedding(content: str):
    embedding = generate_embedding(content)

    engine = get_engine()

    with engine.begin() as connection:
        connection.execute(
            text("""
                INSERT INTO schema_embeddings (content, embedding)
                VALUES (:content, CAST(:embedding AS vector))
            """),
            {
                "content": content,
                "embedding": str(embedding),
            },
        )

    print("Schema embedding stored successfully.")