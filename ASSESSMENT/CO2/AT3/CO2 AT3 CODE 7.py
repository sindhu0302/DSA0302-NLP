from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import re
stemmer = PorterStemmer()
documents = [
    "running runners runs",
    "studies studied studying",
    "organization organized organizer"
]
def preprocess(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return " ".join(stemmer.stem(word) for word in words)
processed = [preprocess(doc) for doc in documents]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(processed)
print("Processed Documents:")
print(processed)
print("Vocabulary:")
print(vectorizer.get_feature_names_out())
print("Feature Matrix:")
print(X.toarray())
