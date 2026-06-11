import faiss
import numpy as np

index = faiss.IndexFlatL2(384)

resume_names = []

def add_resume(name, embedding):
    index.add(np.array([embedding]).astype("float32"))
    resume_names.append(name)

def search(query_embedding, top_k=3):

    distances, indices = index.search(
        np.array([query_embedding]).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        if idx < len(resume_names):
            results.append(resume_names[idx])

    return results