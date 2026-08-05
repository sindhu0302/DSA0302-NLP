# Morphological Parsing

words = ["activate", "activation", "reactivation"]

for word in words:

    prefix = "-"
    suffix = "-"
    root = "activate"
    sequence = ""
    meaning = ""

    if word == "activate":
        sequence = "Base Form"
        meaning = "Perform an action"

    elif word == "activation":
        suffix = "-ion"
        sequence = "activate + ion"
        meaning = "Process of activating"

    elif word == "reactivation":
        prefix = "re-"
        suffix = "-ion"
        sequence = "re + activate + ion"
        meaning = "Activate again"

    print("-"*65)
    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Sequence      :", sequence)
    print("Meaning       :", meaning)
    print("Normalized    :", root)
