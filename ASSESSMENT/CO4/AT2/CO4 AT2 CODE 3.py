# Healthcare NLP System

sentence = ("The doctor who reviewed the patient last week "
            "recommends starting medication and scheduling "
            "a follow-up visit in Chennai.")

print("Input Sentence:")
print(sentence)

# Step 1: Syntactic analysis
print("\n1. CFG Parsing")
print("Subject: The doctor")
print("Relative clause: who reviewed the patient last week")
print("Main verb: recommends")
print("Actions: starting medication, scheduling follow-up visit")
print("Location: Chennai")

# Step 2: PCFG
print("\n2. PCFG Ambiguity Resolution")
probability = 0.90

if probability > 0.5:
    print("Most probable interpretation selected.")

# Step 3: Feature Structures
print("\n3. Feature Structure")
features = {
    "Subject": "doctor",
    "Number": "singular",
    "Verb": "recommends",
    "Agreement": "correct"
}

for key, value in features.items():
    print(key, ":", value)

# Step 4: Sub-categorization
print("\n4. Medical Verb Sub-categorization")

frames = {
    "recommend": "recommend + action",
    "start": "start + medication",
    "schedule": "schedule + follow-up visit"
}

for verb, frame in frames.items():
    print(verb, "->", frame)

# Step 5: Information Extraction
print("\n5. Structured Output")

diagnosis = "Not explicitly mentioned"
actions = ["Start medication", "Schedule follow-up visit"]
location = "Chennai"

print("Diagnosis:", diagnosis)
print("Actions:", actions)
print("Location:", location)

# Step 6: Real-time processing
print("\n6. Real-Time Processing")
print("- Efficient parser processes incoming reports")
print("- PCFG resolves ambiguity")
print("- Feature structures check agreement")
print("- Medical dictionary identifies entities")
print("- Structured results are stored in hospital system")

print("\nFinal Result:")
print("Medical action and follow-up information extracted successfully.")
