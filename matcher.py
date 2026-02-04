from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_match_score(resume_text, jd_text):
    if not resume_text or not jd_text:
        return 0.0

    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, jd_embedding).item()
    return round(max(0, similarity) * 100, 2)

