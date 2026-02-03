import streamlit as st
import fitz  # PyMuPDF

# --------- Helpers ---------
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.lower()

def match_skills(resume_text, jd_text, skills):
    matched = [s for s in skills if s in resume_text and s in jd_text]
    missing = [s for s in skills if s in jd_text and s not in resume_text]
    return matched, missing

# --------- UI ---------
st.set_page_config(page_title="Resume–JD Matcher", layout="wide")
st.title("📄 Resume–Job Description Matcher")

skills = [
    "python", "java", "sql", "machine learning", "deep learning",
    "nlp", "flask", "streamlit", "pandas", "numpy"
]

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description", height=200)

if resume_file and jd_text:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = jd_text.lower()

    matched_skills, missing_skills = match_skills(resume_text, jd_text, skills)

    st.markdown("## ✅ Matched Skills")
    st.write(matched_skills if matched_skills else "No matched skills found")

    st.markdown("## ❌ Missing Skills")
    st.write(missing_skills if missing_skills else "No missing skills 🎉")
