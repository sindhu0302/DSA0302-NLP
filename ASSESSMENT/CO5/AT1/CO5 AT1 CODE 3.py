sentence = "The bank by the river flooded after the storm."

context = ["river", "flooded", "storm"]

# Word Sense Disambiguation
if "river" in context and "flooded" in context:
    bank_meaning = "riverbank"
else:
    bank_meaning = "financial bank"

print("Meaning of bank:", bank_meaning)

# Predicate Logic representation
predicates = [
    "bank(b)",
    "location(b, river)",
    "storm(s)",
    "flood(b)",
    "after(flood(b), s)"
]

print("\nPredicate Logic:")
for predicate in predicates:
    print(predicate)

print("\nParaphrase:")
print("The riverbank flooded after the storm, but quick action saved it.")
