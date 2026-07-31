import pandas as pd

words = ["writes", "writing", "written"]

data = []

for word in words:
    if word == "writes":
        path = "Start -> write -> s"
        root = "write"
        form = "Regular"

    elif word == "writing":
        path = "Start -> write -> ing"
        root = "write"
        form = "Regular"

    elif word == "written":
        path = "Start -> write -> written"
        root = "write"
        form = "Irregular"

    data.append([word, path, root, form, root])

df = pd.DataFrame(data, columns=["Word","State Transition","Root","Pattern","Normalized"])
print(df)
