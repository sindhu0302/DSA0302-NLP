import pandas as pd

words = ["played", "player", "playing"]

data = []

for word in words:
    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        t = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        t = "Derivational"

    data.append([word, stem, affix, t, stem])

df = pd.DataFrame(data, columns=["Word","Stem","Removed Affix","Type","Normalized"])
print(df)
