from sentence_transformers import SentenceTransformer

# Load a lightweight embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str) -> list[float]:
    """
    Convert text into a 384-dimensional vector.
    """
    embedding = model.encode(text)

    return embedding.tolist()