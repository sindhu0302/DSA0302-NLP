# Ambiguity Handling

sentence = "She saw the man with a telescope"

print("Sentence:", sentence)

print("\nPossible meanings:")
print("1. She used a telescope to see the man.")
print("2. The man had a telescope.")

print("\nCFG:")
print("Generates both possible parse structures.")
print("Cannot easily decide the correct one.")

print("\nPCFG:")
print("Assigns probabilities to different parse structures.")
print("Selects the most probable interpretation.")

print("\nNeural Parsing:")
print("Uses learned language patterns and context.")
print("Can select the most suitable interpretation.")

# Simple probability example
cfg_parse1 = 0.4
cfg_parse2 = 0.6

print("\nPCFG probabilities:")
print("Meaning 1:", cfg_parse1)
print("Meaning 2:", cfg_parse2)

if cfg_parse1 > cfg_parse2:
    print("Selected Meaning: She used a telescope.")
else:
    print("Selected Meaning: The man had a telescope.")

print("\nConclusion:")
print("Neural parsing is generally more effective for real-world NLP.")
