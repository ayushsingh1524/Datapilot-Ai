from src.ai.embeddings import generate_embedding


text = "The orders table contains product, price, quantity and revenue data."

embedding = generate_embedding(text)

print("Embedding generated successfully.")
print("Number of dimensions:", len(embedding))
print("First 5 values:", embedding[:5])