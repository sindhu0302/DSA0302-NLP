import re

text = "John went to the shop. He bought milk."

sentences = text.split(".")
first = sentences[0]
second = sentences[1]

name = re.search(r'\b[A-Z][a-z]+\b', first).group()
pronoun = re.search(r'\b(He|She|They)\b', second).group()

print("Pronoun:", pronoun)
print("Refers to:", name)
