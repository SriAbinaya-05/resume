import os

from utils.pdf_loader import load_pdf
from utils.embeddings import get_embedding
from utils.ranking import rank_resume
from utils.retriever import add_resume

JOB_DESCRIPTION = """
Python
Java
SQL
Machine Learning
Data Analysis
"""

print("Resume Screening RAG Started\n")

resume_folder = "resumes"

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        path = os.path.join(resume_folder, file)

        text = load_pdf(path)

        embedding = get_embedding(text)

        add_resume(file, embedding)

        score = rank_resume(
            text,
            JOB_DESCRIPTION
        )

        print(f"Resume : {file}")
        print(f"Score  : {score}")
        print("-" * 40)

print("\nProcessing Completed")