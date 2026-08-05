# Inflectional Morphology Normalization

words = ["create", "creates", "creating"]

for word in words:

    suffix = "-"
    grammar = "Base Form"
    root = "create"

    if word.endswith("s"):
        suffix = "-s"
        grammar = "Third Person Singular"

    elif word.endswith("ing"):
        suffix = "-ing"
        grammar = "Present Participle"

    print("-"*60)
    print("Original Word :", word)
    print("Suffix        :", suffix)
    print("Grammar       :", grammar)
    print("Root Word     :", root)
    print("Normalized    :", root)
