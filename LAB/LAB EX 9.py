import re

sentence = input("Enter a sentence: ")

for word in sentence.split():
    if re.match(r'.*ing$', word):
        tag = "VBG"
    elif re.match(r'.*ly$', word):
        tag = "RB"
    else:
        tag = "NN"
    print(word, "->", tag)
