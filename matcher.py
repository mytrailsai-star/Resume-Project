from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import re

# ---------- PDF READER ----------
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return clean_text(text)

# ---------- TEXT CLEANER ----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text

# ---------- MATCH SCORE ----------
def calculate_match(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)

# ---------- SKILL COMPARISON ----------
def compare_skills(jd_text, resume_text):
    skills = [
        "python", "sql", "machine learning", "deep learning",
        "nlp", "data analysis", "pandas", "numpy", "scikit-learn",
        "flask", "streamlit", "git", "docker", "api", "aws"
    ]

    jd_words = jd_text.lower()
    resume_words = resume_text.lower()

    matched = [s for s in skills if s in resume_words and s in jd_words]
    missing = [s for s in skills if s in jd_words and s not in resume_words]

    return {
        "matched": matched,
        "missing": missing
    }
