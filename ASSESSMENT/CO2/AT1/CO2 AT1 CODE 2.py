import pandas as pd

words = ["unhappy", "happiness", "happily"]

data = []

for word in words:
    prefix = ""
    suffix = ""
    base = "happy"

    if word.startswith("un"):
        prefix = "un"
        suffix = "-"
        t = "Derivational"

    elif word.endswith("ness"):
        suffix = "ness"
        t = "Derivational"

    elif word.endswith("ly"):
        suffix = "ly"
        t = "Derivational"

    data.append([word, prefix, base, suffix, t, base])

df = pd.DataFrame(data, columns=["Word","Prefix","Base","Suffix","Type","Normalized"])
print(df)
