import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    words = text.split()
    words = [stemmer.stem(w) for w in words
             if w not in ENGLISH_STOP_WORDS and len(w) > 2]
    return " ".join(words)