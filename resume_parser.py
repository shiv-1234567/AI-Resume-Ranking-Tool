import fitz  # PyMuPDF

import spacy




nlp = spacy.load("en_core_web_sm")

# Define basic skill and education keyword lists
SKILL_KEYWORDS = [
    "python", "c++", "java", "sql", "machine learning", "deep learning", 
    "nlp", "pandas", "numpy", "excel", "tensorflow", "keras", "scikit-learn"
]

EDUCATION_KEYWORDS = [
    "b.tech", "m.tech", "bachelor", "master", "msc", "phd", 
    "bsc", "ba", "be", "mca", "bca", "graduation", "degree"
]

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using PyMuPDF (fitz)."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"[ERROR] Could not read PDF: {e}")
    return text

def extract_entities(text):
    """Extract named entities + custom skills, education, experience, and projects keywords."""
    doc = nlp(text)

    entities = {
        "PERSON": set(),
        "ORG": set(),
        "GPE": set(),
        "EDUCATION": set(),
        "SKILLS": set(),
        "EXPERIENCE": set(),  
        "PROJECTS": set()     
    }

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].add(ent.text.strip())

    # Convert to lowercase for keyword matching
    text_lower = text.lower()

    # Add keyword-matched entries
    entities["SKILLS"].update({skill for skill in SKILL_KEYWORDS if skill in text_lower})
    entities["EDUCATION"].update({edu for edu in EDUCATION_KEYWORDS if edu in text_lower})

    # Basic heuristic (optional): match lines with "project", "experience", etc.
    for line in text_lower.split("\n"):
        if "experience" in line:
            entities["EXPERIENCE"].add(line.strip())
        if "project" in line:
            entities["PROJECTS"].add(line.strip())

    # Convert sets to sorted lists for output
    return {k: sorted(list(v)) for k, v in entities.items()}
