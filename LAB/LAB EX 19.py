from nltk.wsd import lesk

sentence = "I went to the bank to deposit money"
words = sentence.split()

sense = lesk(words, "bank")

print("Word:", sense.name())
print("Meaning:", sense.definition())
