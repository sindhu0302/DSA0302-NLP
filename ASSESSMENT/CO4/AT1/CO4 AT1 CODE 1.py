# Semantic Representation

queries = {
    "Q1": ("ACTIVATE", "Roaming"),
    "Q2": ("DEACTIVATE", "CallerTune"),
    "Q3": ("QUERY", "DataBalance"),
    "Q4": ("ACTIVATE", "5GService")
}

actual = {
    "Q1": "ACTIVATE Roaming",
    "Q2": "DEACTIVATE CallerTune",
    "Q3": "QUERY DataBalance",
    "Q4": "ACTIVATE 5GService"
}

predicted = {
    "Q1": "ACTIVATE Roaming",
    "Q2": "ACTIVATE CallerTune",   # Error
    "Q3": "QUERY DataBalance",
    "Q4": "ACTIVATE 5GService"
}

for q in queries:
    print(q, ":", queries[q])

print("\nErrors:")
for q in actual:
    if actual[q] != predicted[q]:
        print(q, "has semantic interpretation error")

accuracy = sum(actual[q] == predicted[q] for q in actual) / len(actual) * 100
print("Accuracy:", accuracy, "%")
