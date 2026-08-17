# CFG vs Dependency Parsing

sentence = "The student reads a book"

print("Sentence:", sentence)

# CFG representation
print("\nCFG Tree:")
print("S")
print("|-- NP -> The student")
print("|-- VP")
print("    |-- V -> reads")
print("    |-- NP -> a book")

# Dependency representation
print("\nDependency Structure:")
print("reads -> student (subject)")
print("reads -> book (object)")
print("student -> The (determiner)")
print("book -> a (determiner)")

print("\nConclusion:")
print("CFG shows phrase structure.")
print("Dependency parsing shows direct word relationships.")
print("Dependency parsing is better for capturing word-to-word relationships.")
