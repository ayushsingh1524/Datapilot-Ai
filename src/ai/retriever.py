from sqlalchemy import text

from src.ai.embeddings import generate_embedding
from src.database.connection import get_engine


def retrieve_relevant_schema(question: str, limit: int = 3) -> list[str]:
    """
    Find the most relevant schema documentation
    using vector similarity.
    """

    question_embedding = generate_embedding(question)

    engine = get_engine()

    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT content
                FROM schema_embeddings
                ORDER BY embedding <=> CAST(:embedding AS vector)
                LIMIT :limit
            """),
            {
                "embedding": str(question_embedding),
                "limit": limit,
            },
        )

        rows = result.fetchall()

    return [row[0] for row in rows]
