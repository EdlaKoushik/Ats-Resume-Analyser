#preprocessing
# backend/core/preprocessing.py
import re


def clean_text(text: str) -> list:
    text = text.lower()
    text = re.sub(r'[^a-z]', ' ', text)
    words = text.split()
    return words

# Preprocessing normalizes textual variations so that semantically identical skills are treated consistently during vectorization and similarity computation.


