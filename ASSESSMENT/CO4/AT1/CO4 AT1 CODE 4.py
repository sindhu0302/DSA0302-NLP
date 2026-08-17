# Syntax-Driven Semantic Analysis

sentences = {
    "Doctor prescribed medicine to patient":
        {"Doctor": "Agent", "Medicine": "Theme", "Patient": "Recipient"},

    "Patient reported severe headache":
        {"Patient": "Experiencer", "Headache": "Symptom"},

    "Nurse monitored patient":
        {"Nurse": "Agent", "Patient": "Object"},

    "Medicine reduced blood pressure":
        {"Medicine": "Cause", "Blood Pressure": "Theme"}
}

for sentence, roles in sentences.items():
    print("\nSentence:", sentence)

    for entity, role in roles.items():
        print(entity, "->", role)
