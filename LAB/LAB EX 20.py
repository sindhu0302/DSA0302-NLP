from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "machine learning is useful",
    "python is useful for machine learning",
    "cats and dogs are animals"
]

query = ["machine learning"]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents + query)

scores = cosine_similarity(vectors[-1], vectors[:-1])

for i, score in enumerate(scores[0]):
    print("Document", i + 1, ":", round(score, 2))
