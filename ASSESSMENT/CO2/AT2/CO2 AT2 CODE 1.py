# Morphological Processing - Rule Based

words = ["analyzing", "analysis", "analytical"]

for word in words:
    root = ""
    affix = ""
    transformation = ""

    if word.endswith("ing"):
        root = word[:-3]
        affix = "-ing"
        transformation = "Inflectional"

    elif word.endswith("sis"):
        root = "analyze"
        affix = "-sis"
        transformation = "Derivational"

    elif word.endswith("ical"):
        root = "analyze"
        affix = "-ical"
        transformation = "Derivational"

    print("-" * 60)
    print("Original Word :", word)
    print("Root Word     :", root)
    print("Affix         :", affix)
    print("Type          :", transformation)
    print("Normalized    :", "analyze")
