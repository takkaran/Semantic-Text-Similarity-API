from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(text1: str, text2: str) -> float:
    """Returns similarity score (0-1) as per assessment specs"""
    embeddings = model.encode([text1, text2], convert_to_tensor=True)
    return float(util.cos_sim(embeddings[0], embeddings[1]).item())
