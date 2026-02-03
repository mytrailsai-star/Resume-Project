import streamlit as st
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import numpy as np

from flask import Flask, render_template, request
from matcher import calculate_match, read_pdf, compare_skills

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    results = []
    matched_skills = []
    missing_skills = []

    if request.method == "POST":
        jd_text = request.form["jd"]
        files = request.files.getlist("resumes")

        for file in files:
            resume_text = read_pdf(file)
            score = calculate_match(resume_text, jd_text)
            skill_result = compare_skills(jd_text, resume_text)

            results.append({
                "name": file.filename,
                "score": score
            })

            matched_skills = skill_result["matched_skills"]
            missing_skills = skill_result["missing_skills"]

        results = sorted(results, key=lambda x: x["score"], reverse=True)

    return render_template(
        "index.html",
        score=score,
        results=results,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )

if __name__ == "__main__":
    app.run(debug=True)
