from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# Get input from the user
text = input("Enter a word or sentence: ")

# Split the sentence into words
words = text.split()

# Apply stemming
stemmed_words = []
for word in words:
    stemmed_words.append(ps.stem(word))

# Join the stemmed words
result = " ".join(stemmed_words)

# Display results
print("\nOriginal Text : ", text)
print("Stemmed Text  : ", result)
