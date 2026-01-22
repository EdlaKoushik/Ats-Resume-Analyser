# backend/core/vectorizer.py
from sklearn.feature_extraction.text import TfidfVectorizer
from core.preprocessing import clean_text


def vectorize_texts(resume_text: str, jd_text: str):
    resume_tokens = clean_text(resume_text)
    jd_tokens = clean_text(jd_text)

    resume_clean = " ".join(resume_tokens)
    jd_clean = " ".join(jd_tokens)

    documents = [resume_clean, jd_clean]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    resume_vector = tfidf_matrix[0].toarray()[0]
    jd_vector = tfidf_matrix[1].toarray()[0]

    return resume_vector, jd_vector





