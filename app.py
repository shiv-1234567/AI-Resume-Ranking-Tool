import streamlit as st
import pandas as pd
from resume_parser import extract_text_from_pdf, extract_entities
from matcher import calculate_similarity
from utils import save_uploaded_files

st.set_page_config(page_title="Resume Screening Tool", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>📄 AI-Powered Resume Screening Tool</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Job Description Section
st.markdown("### 🧾 Job Description")
jd_input = st.text_area("Paste the Job Description", height=200)

# Resume Upload Section
st.markdown("### 📤 Upload Resume PDFs")
uploaded_files = st.file_uploader("Upload Resumes", type=["pdf"], accept_multiple_files=True)

# Rank Button
if st.button("🚀 Rank Candidates"):
    if not uploaded_files or not jd_input:
        st.warning("⚠️ Please upload resumes and provide a job description.")
    else:
        file_paths = save_uploaded_files(uploaded_files)

        resume_texts = []
        extracted_entities = []

        for fp in file_paths:
            text = extract_text_from_pdf(fp)
            resume_texts.append(text)
            extracted_entities.append(extract_entities(text))

        scores = calculate_similarity(resume_texts, job_description=jd_input)

        data = {
            "Candidate": [f.name for f in uploaded_files],
            "Score": scores,
            "Skills": [", ".join(e["SKILLS"]) for e in extracted_entities],
            "Education": [", ".join(e["EDUCATION"]) for e in extracted_entities],
            "Experience": [", ".join(e.get("EXPERIENCE", [])) for e in extracted_entities],
            "Projects": [", ".join(e.get("PROJECTS", [])) for e in extracted_entities]
        }

        df = pd.DataFrame(data)
        df.sort_values(by="Score", ascending=False, inplace=True)

        st.success("✅ Ranking completed!")
        st.markdown("### 🏆 Ranked Candidates")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Ranking as CSV", data=csv, file_name="ranking.csv", mime='text/csv')

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; color: gray;'>© 2025 Shivendra Prasad Mishra. All rights reserved.</div>",
    unsafe_allow_html=True
)
