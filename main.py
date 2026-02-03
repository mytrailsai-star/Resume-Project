
from sentence_transformers import SentenceTransformer, util
import os

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read job description
with open("data/jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

jd_embedding = model.encode(jd_text, convert_to_tensor=True)

resumes_path = "data/resumes"
results = []

# Process each resume
for file_name in os.listdir(resumes_path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(resumes_path, file_name)

        with open(file_path, "r", encoding="utf-8") as f:
            resume_text = f.read()

        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        score = util.cos_sim(resume_embedding, jd_embedding)
        match_percentage = float(score[0][0]) * 100

        results.append((file_name, match_percentage))

# Sort results
results.sort(key=lambda x: x[1], reverse=True)

print("\n📊 Resume Ranking:\n")
for i, (name, score) in enumerate(results, start=1):
    print(f"{i}. {name} → {score:.2f}%")
