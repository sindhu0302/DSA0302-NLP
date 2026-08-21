text = "Ravi met Arun at the library. He borrowed a book and later returned it."

# Identified entities
entities = ["Ravi", "Arun", "book"]

# Reference resolution
references = {
    "He": "Ravi",
    "it": "book"
}

print("Reference Resolution:")
for pronoun, entity in references.items():
    print(pronoun, "->", entity)

# Resolved discourse
resolved = (
    "Ravi met Arun at the library. "
    "Ravi borrowed a book and later returned the book."
)

print("\nResolved Discourse:")
print(resolved)
