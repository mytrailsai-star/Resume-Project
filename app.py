from skills import SKILLS

import streamlit as st
import fitz  # PyMuPDF
import pandas as pd

# --------- Helpers ---------
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.lower()

def match_SKILLS(resume_text, jd_text, SKILLS):
    matched = [s for s in SKILLS if s in resume_text and s in jd_text]
    missing = [s for s in SKILLS if s in jd_text and s not in resume_text]
    return matched, missing

# --------- UI ---------
st.set_page_config(page_title="Resume–JD Matcher", layout="wide")
st.title("📄 Resume–Job Description Matcher")

SKILLS = [
    "python", "java", "sql", "machine learning", "deep learning",
    "nlp", "flask", "streamlit", "pandas", "numpy"
]

resume_files = st.file_uploader(
    "Upload Resumes (PDFs)",
    type=["pdf"],
    accept_multiple_files=True
)

jd_text = st.text_area("Paste Job Description", height=200)

if resume_files and jd_text:
    jd_text = jd_text.lower()
    results = []

    for resume in resume_files:
        resume_text = extract_text_from_pdf(resume)
        matched, missing = match_SKILLS(resume_text, jd_text, SKILLS)

        total_required = len([s for s in SKILLS if s in jd_text])
        score = int((len(matched) / total_required) * 100) if total_required else 0

        results.append({
            "Resume": resume.name,
            "Match %": score,
            "Matched SKILLS": ", ".join(matched),
            "Missing SKILLS": ", ".join(missing)
        })

    df = pd.DataFrame(results).sort_values(by="Match %", ascending=False)

    st.markdown("## 📊 Resume Ranking")
    st.dataframe(df, use_container_width=True)

