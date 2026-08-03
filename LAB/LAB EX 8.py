tag_dict = {
    "I": "PRP",
    "eat": "VB",
    "apple": "NN",
    "an": "DT"
}

sentence = input("Enter a sentence: ")

for word in sentence.split():
    tag = tag_dict.get(word, "NN")
    print(word, "->", tag)
