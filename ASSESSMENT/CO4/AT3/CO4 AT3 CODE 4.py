# Feature Structures and Subcategorization Frames

print("Feature Structure Example:")

features = {
    "Subject": "She",
    "Number": "Singular",
    "Verb": "runs",
    "Verb_Number": "Singular"
}

for key, value in features.items():
    print(key, ":", value)

if features["Number"] == features["Verb_Number"]:
    print("Subject-Verb Agreement: Correct")

print("\nSubcategorization Frame:")

frames = {
    "eat": "eat + object",
    "give": "give + object + recipient",
    "sleep": "sleep + no object"
}

for verb, frame in frames.items():
    print(verb, "->", frame)

print("\nConclusion:")
print("Feature structures are better for enforcing grammatical agreement.")
print("Subcategorization frames are useful for checking verb arguments.")
print("Using both provides better grammatical analysis.")
