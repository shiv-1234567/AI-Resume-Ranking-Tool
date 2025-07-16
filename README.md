# AI-Resume-Ranking-Tool
🧠 AI-Powered Resume Screening Tool
This project is an intelligent, Streamlit-based web application that assists recruiters, HR professionals, and hiring managers in efficiently ranking job applicants by analyzing and scoring resumes based on a given job description.

It leverages Natural Language Processing (NLP) using spaCy, TF-IDF vectorization, and cosine similarity to compute how well a resume matches the job requirements in terms of skills, education, experience, and projects.

🚀 Features
✅ Upload multiple resumes in PDF format
✅ Paste a job description in plain text
✅ Automatically extract skills, education, experience, and project info from each resume using spaCy
✅ Assign weights to different resume sections for smarter scoring
✅ Ranks candidates based on semantic similarity with job description
✅ Display and download a detailed ranking report as a CSV
✅ Clean, interactive Streamlit web interface
✅ Custom footer and styling for branding

🛠️ Tech Stack
Tool	Description
Python	Core programming language
spaCy	Named Entity Recognition and NLP
PyMuPDF (fitz)	PDF text extraction
scikit-learn	TF-IDF and cosine similarity
pandas	Data manipulation and tabular output
Streamlit	Web-based UI for interaction

📈 Scoring Logic (Custom Weighted)
Each resume is scored based on:

Skills and Education (core TF-IDF cosine similarity)

Bonus for Experience mentions (e.g., 0.02 points per experience keyword)

Bonus for Project mentions (e.g., 0.01 points per project keyword)

This provides a weighted similarity score for a more realistic candidate ranking.

📷 Screenshots
Home Interface	
<img width="1050" height="832" alt="image" src="https://github.com/user-attachments/assets/c9feb849-9603-4d59-948c-f0745a4a325b" />


Ranking Output
<img width="1034" height="852" alt="image" src="https://github.com/user-attachments/assets/c70cc595-53f9-48f3-b945-ffb60663735c" />

📌 Future Improvements
✅ Use GPT-based embedding for smarter semantic matching

✅ Support DOCX formats

✅ Add UI filters for years of experience

✅ Deploy on Streamlit Cloud or Hugging Face Spaces



#👨‍💻 Author
Shivendra Prasad Mishra
Master’s Student, IIT Delhi | Data Science & AI Enthusiast

📄 License
This project is licensed under the MIT License 
