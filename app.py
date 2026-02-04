import streamlit as st
from matcher import get_match_score
from skills import extract_skills

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Resume–JD Matcher",
    layout="wide"
)

st.title("📄 Resume ↔ Job Description Matcher")
st.caption("AI-powered resume screening using NLP & Transformer embeddings")

# ---------------- HELPER FUNCTION ----------------
def render_skill_tags(skills, color):
    if not skills:
        return

    tags_html = ""
    for skill in skills:
        tags_html += f"""
        <span style="
            display:inline-block;
            padding:6px 12px;
            margin:4px;
            border-radius:20px;
            background-color:{color};
            color:white;
            font-size:14px;
        ">
            {skill}
        </span>
        """

    st.markdown(tags_html, unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧑‍💼 Resume Text")
    resume_text = st.text_area(
        "Paste resume content here",
        height=300,
        placeholder="Paste resume text..."
    )

with col2:
    st.subheader("📌 Job Description")
    jd_text = st.text_area(
        "Paste job description here",
        height=300,
        placeholder="Paste job description text..."
    )

st.divider()

# ---------------- ACTION SECTION ----------------
if st.button("🔍 Analyze Match", use_container_width=True):

    if resume_text.strip() and jd_text.strip():

        with st.spinner("Analyzing resume against job description..."):
            match_score = get_match_score(resume_text, jd_text)
            matched_skills, missing_skills = extract_skills(resume_text, jd_text)

        st.success("Analysis complete!")

        # ---------------- MATCH SCORE ----------------
        st.subheader("📊 Match Score")
        st.progress(match_score / 100)
        st.metric("Overall Resume–JD Match", f"{match_score:.2f}%")

        st.divider()

        # ---------------- SKILLS SECTION ----------------
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Matched Skills")
            if matched_skills:
                render_skill_tags(matched_skills, "#2ecc71")  # green
            else:
                st.info("No matched skills found")

        with col4:
            st.subheader("❌ Missing Skills")
            if missing_skills:
                render_skill_tags(missing_skills, "#e74c3c")  # red
            else:
                st.success("No missing skills 🎉")

    else:
        st.warning("Please paste both Resume and Job Description text.")

  