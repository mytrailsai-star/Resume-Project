import streamlit as st

st.set_page_config(
    page_title="Resume–JD Matcher",
    layout="wide"
)

st.title("📄 Resume ↔ Job Description Matcher")
st.caption("AI-powered resume screening using NLP & embeddings")

# --- INPUT SECTION ---
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

# --- ACTION ---
if st.button("🔍 Analyze Match", use_container_width=True):
    if resume_text and jd_text:

        with st.spinner("Analyzing resume against JD..."):
            match_score = get_match_score(resume_text, jd_text)
            matched_skills, missing_skills = extract_skills(resume_text, jd_text)

        st.success("Analysis complete!")

        # --- SCORE ---
        st.subheader("📊 Match Score")
        st.progress(match_score / 100)
        st.metric("Overall Match", f"{match_score:.2f}%")

        # --- SKILLS ---
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Matched Skills")
            if matched_skills:
                st.write(", ".join(matched_skills))
            else:
                st.info("No matched skills found")

        with col4:
            st.subheader("❌ Missing Skills")
            if missing_skills:
                st.write(", ".join(missing_skills))
            else:
                st.success("No missing skills 🎉")

    else:
        st.warning("Please paste both Resume and Job Description.")

