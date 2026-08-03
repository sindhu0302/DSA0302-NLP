import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The cat is sleeping on the mat."

words = word_tokenize(text)
tags = nltk.pos_tag(words)

print(tags)
