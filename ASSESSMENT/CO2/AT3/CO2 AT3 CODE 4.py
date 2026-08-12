from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = [
    "watches",
    "watching",
    "washable",
    "washer",
    "washed"
]
derivational = ["washable", "washer"]
for word in words:
    stem = ps.stem(word)
    if word in derivational:
        morphology = "Derivational"
    else:
        morphology = "Inflectional"
    print("Word:", word)
    print("Stem:", stem)
    print("Type:", morphology)
    print()
