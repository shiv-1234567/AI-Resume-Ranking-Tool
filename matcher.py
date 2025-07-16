from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from resume_parser import extract_entities

def calculate_similarity(resume_texts, job_description):
    jd_entities = extract_entities(job_description)
    jd_keywords = ' '.join(jd_entities['SKILLS'] + jd_entities['EDUCATION'])

    scores = []

    for resume in resume_texts:
        resume_entities = extract_entities(resume)
        resume_keywords = ' '.join(resume_entities['SKILLS'] + resume_entities['EDUCATION'])

        # Compute base similarity
        documents = [jd_keywords, resume_keywords]
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0][0]

        # Add weighted bonuses
        experience_bonus = min(len(resume_entities["EXPERIENCE"]), 10) * 0.01  # up to +0.10
        project_bonus = min(len(resume_entities["PROJECTS"]), 5) * 0.01        # up to +0.05

        total_score = similarity + experience_bonus + project_bonus
        scores.append(round(total_score, 3))

    return scores
