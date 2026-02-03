import streamlit as st
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util
import numpy as np

st.set_page_config(page_title="Resume–JD Matcher", layout="wide")

st.title("📄 Resume – Job Description Matcher")

st.write("Upload resumes and paste a Job Description to see match score, matched skills, and missing skills.")

jd_text = st.text_area("Paste Job Description here")

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Match Resumes") and jd_text and uploaded_files:
    st.info("Processing resumes...")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    for file in uploaded_files:
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            resume_text = ""
            for page in doc:
                resume_text += page.get_text()

        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        score = util.cos_sim(jd_embedding, resume_embedding).item()

        st.subheader(file.name)
        st.write(f"✅ Match Score: **{score:.2f}**")

