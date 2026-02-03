import streamlit as st
import fitz  # PyMuPDF
import numpy as np

st.set_page_config(page_title="Resume–JD Matcher", layout="wide")

st.title("📄 Resume–Job Description Matcher")

st.markdown("### Upload Resume (PDF)")
resume_file = st.file_uploader("Upload Resume", type=["pdf"])

st.markdown("### Paste Job Description")
jd_text = st.text_area("Job Description", height=200)

if resume_file and jd_text:
    st.success("Inputs received successfully ✅")
    st.info("Next: skill extraction & matching")


