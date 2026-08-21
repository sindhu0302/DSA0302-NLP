sentences = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

relations = [
    ("Sentence 1", "Sentence 2", "Cause-Effect"),
    ("Sentence 2", "Sentence 3", "Sequence/Result")
]

print("Discourse Relations:")
for source, target, relation in relations:
    print(source, "->", target, ":", relation)

print("\nDiscourse Structure:")
print("Heavy rainfall")
print("     ↓")
print("Roads flooded")
print("     ↓ Cause-Effect")
print("Schools closed")
print("     ↓ Sequence/Result")
print("Students attended online classes")
