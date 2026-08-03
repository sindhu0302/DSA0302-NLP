sentence = input("Enter a sentence: ")

for word in sentence.split():
    tag = "NN"   # Initial tag

    if word.lower() in ["is", "am", "are"]:
        tag = "VB"
    elif word.endswith("ing"):
        tag = "VBG"

    print(word, "->", tag)
