text = "I love natural language processing"

words = text.split()

bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]

print("Bigrams:", bigrams)

generated = words[0]
for pair in bigrams:
    generated += " " + pair[1]

print("Generated Text:", generated)
