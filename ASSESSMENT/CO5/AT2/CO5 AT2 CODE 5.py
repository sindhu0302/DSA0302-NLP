source = "The boy is playing football."

# Step 1: Source analysis
semantic = {
    "agent": "boy",
    "action": "play",
    "object": "football",
    "tense": "present_continuous"
}

# Step 2: Interlingua
interlingua = (
    "PLAY(AGENT=BOY, OBJECT=FOOTBALL, "
    "TENSE=PRESENT_CONTINUOUS)"
)

# Step 3: Candidate translations with statistical scores
candidates = {
    "சிறுவன் கால்பந்து விளையாடுகிறான்.": 0.92,
    "சிறுவன் கால்பந்து விளையாடினான்.": 0.05,
    "சிறுவன் கால்பந்து விளையாடுவான்.": 0.03
}

# Step 4: Select highest-scoring translation
best_translation = max(candidates, key=candidates.get)

print("Source Sentence:")
print(source)

print("\nInterlingua:")
print(interlingua)

print("\nCandidate Translations:")
for sentence, score in candidates.items():
    print(sentence, "->", score)

print("\nFinal Translation:")
print(best_translation)
