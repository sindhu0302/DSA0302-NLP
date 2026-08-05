# Morphological Parser

words = ["disagree", "agreement", "agreeable"]

for word in words:

    prefix = "-"
    suffix = "-"
    root = "agree"
    category = ""
    meaning = ""

    if word.startswith("dis"):
        prefix = "dis-"
        category = "Derivational"
        meaning = "Negative meaning"

    elif word.endswith("ment"):
        suffix = "-ment"
        category = "Derivational"
        meaning = "State or result"

    elif word.endswith("able"):
        suffix = "-able"
        category = "Derivational"
        meaning = "Capable of"

    print("-"*65)
    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Category      :", category)
    print("Meaning       :", meaning)
    print("Normalized    :", root)
