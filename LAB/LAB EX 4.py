word = input("Enter a noun: ")

if word.endswith("y"):
    plural = word[:-1] + "ies"
else:
    plural = word + "s"

print("Plural:", plural)
