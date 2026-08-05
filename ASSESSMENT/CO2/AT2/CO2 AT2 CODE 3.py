# Morphology Based Normalization

words = ["govern", "government", "governance"]

for word in words:

    root = "govern"
    affix = "-"
    level = "Base"

    if word.endswith("ment"):
        affix = "-ment"
        level = "Level 1 Derivation"

    elif word.endswith("ance"):
        affix = "-ance"
        level = "Level 1 Derivation"

    print("-"*60)
    print("Original Word :", word)
    print("Root Word     :", root)
    print("Affix         :", affix)
    print("Hierarchy     :", level)
    print("Normalized    :", root)
