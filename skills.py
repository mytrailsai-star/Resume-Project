import re

SKILLS_DB = [
    "python", "java", "sql", "machine learning", "deep learning",
    "nlp", "data science", "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch", "transformers", "streamlit",
    "flask", "git", "github", "docker", "aws"
]

def extract_skills(resume_text, jd_text):
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    resume_skills = set()
    jd_skills = set()

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume_text):
            resume_skills.add(skill)
        if re.search(pattern, jd_text):
            jd_skills.add(skill)

    matched_skills = sorted(resume_skills & jd_skills)
    missing_skills = sorted(jd_skills - resume_skills)

    return matched_skills, missing_skills
