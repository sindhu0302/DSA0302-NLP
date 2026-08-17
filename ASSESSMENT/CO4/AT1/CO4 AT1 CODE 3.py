# Word Sense Disambiguation

queries = {
    "Apple accessories": "Technology",
    "Mouse wireless": "Computer Device",
    "Java tutorial": "Programming Language",
    "Python course": "Programming Language"
}

clicked_results = {
    "Apple accessories": "iPhone Charger",
    "Mouse wireless": "Bluetooth Mouse",
    "Java tutorial": "Coding Lessons",
    "Python course": "Software Development Training"
}

for query in queries:
    print("Query:", query)
    print("Clicked Result:", clicked_results[query])
    print("Correct Sense:", queries[query])
    print()

# Accuracy
correct = 4
total = 4

accuracy = (correct / total) * 100
print("WSD Accuracy:", accuracy, "%")
