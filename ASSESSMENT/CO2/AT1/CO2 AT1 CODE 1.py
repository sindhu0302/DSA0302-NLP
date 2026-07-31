import pandas as pd

words = ["connected", "connecting", "connection"]

data = []

for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        t = "Inflectional"
        norm = "connect"
    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        t = "Inflectional"
        norm = "connect"
    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        t = "Derivational"
        norm = "connect"

    data.append([word, root, suffix, t, norm])

df = pd.DataFrame(data, columns=["Word","Root","Suffix","Type","Normalized"])
print(df)
