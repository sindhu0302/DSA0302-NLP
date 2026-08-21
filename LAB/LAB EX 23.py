text = [
    "I like natural language processing",
    "Natural language processing is useful"
]

words1 = set(text[0].lower().split())
words2 = set(text[1].lower().split())

common = words1.intersection(words2)

score = len(common)

print("Common words:", common)
print("Coherence Score:", score)
