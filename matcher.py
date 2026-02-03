from sentence_transformers import SentenceTransformer, util
import fitz  # PyMuPDF

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def calculate_match(resume_text, jd_text):
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    jd_emb = model.encode(jd_text, convert_to_tensor=True)
    score = util.cos_sim(resume_emb, jd_emb).item()
    return round(score * 100, 2)

def read_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text
from skills import SKILLS
import re

def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return list(found_skills)
def compare_skills(jd_text, resume_text):
    jd_skills = set(extract_skills(jd_text))
    resume_skills = set(extract_skills(resume_text))

    matched = list(jd_skills & resume_skills)
    missing = list(jd_skills - resume_skills)

    return {
        "jd_skills": list(jd_skills),
        "resume_skills": list(resume_skills),
        "matched_skills": matched,
        "missing_skills": missing
    }
