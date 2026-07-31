from nltk.stem import PorterStemmer
import pandas as pd

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

data = []

for word in words:
    if word == "relational":
        rule = "Remove 'ational'"
        intermediate = "relate"

    elif word == "relation":
        rule = "Remove 'ion'"
        intermediate = "relat"

    else:
        rule = "Remove 'e'"
        intermediate = "relat"

    stem = ps.stem(word)

    data.append([word, rule, intermediate, stem])

df = pd.DataFrame(data, columns=["Word","Rule Applied","Intermediate Form","Final Stem"])
print(df)
