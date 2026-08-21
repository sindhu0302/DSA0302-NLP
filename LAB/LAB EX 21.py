sentence = "The student reads a book"

noun_phrases = ["The student", "a book"]

meanings = {
    "The student": "a person who studies",
    "a book": "a written document"
}

for phrase in noun_phrases:
    print(phrase, "->", meanings[phrase])