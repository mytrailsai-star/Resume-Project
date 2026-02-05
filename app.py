from flask import Flask, render_template, request
from matcher import calculate_match, read_pdf, compare_skills

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    rankings = []
    skills_result = None

    if request.method == "POST":
        jd_text = request.form.get("jd", "").strip()
        files = request.files.getlist("resumes")

        if jd_text and files:
            resume_texts = []

            for file in files:
                resume_text = read_pdf(file)
                resume_texts.append((file.filename, resume_text))

                score = calculate_match(resume_text, jd_text)
                rankings.append({
                    "name": file.filename,
                    "score": round(score, 2)
                })

            # Sort resumes by match score
            rankings.sort(key=lambda x: x["score"], reverse=True)

            # Compare skills ONLY for top-ranked resume
            top_resume_text = resume_texts[0][1]
            skills_result = compare_skills(jd_text, top_resume_text)

    return render_template(
        "index.html",
        rankings=rankings,
        skills=skills_result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



    
    


  