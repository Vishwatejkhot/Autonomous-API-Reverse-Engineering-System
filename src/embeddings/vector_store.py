import os
import faiss
import numpy as np

class VectorStore:
    def __init__(self, embed_model):
        self.embed_model = embed_model
        self.index = None
        self.embeddings = None

    def save(self):
        if self.index:
            faiss.write_index(self.index, "vector_store.index")

    def load(self):
        if os.path.exists("vector_store.index"):
            self.index = faiss.read_index("vector_store.index")
            return True
        return False

    def build(self, texts):
        emb = self.embed_model.encode(texts, normalize_embeddings=True).astype("float32")
        dim = emb.shape[1]

        index = faiss.IndexFlatIP(dim)
        index.add(emb)

        self.index = index
        self.embeddings = emb
        self.save()

    def search(self, query, k=8):
        q_emb = self.embed_model.encode([query], normalize_embeddings=True).astype("float32")
        scores, idx = self.index.search(q_emb, k)
        return scores[0], idx[0]
