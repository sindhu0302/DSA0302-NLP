# Q1: POS tagging

sentence1 = [
    ("Book", "VB"),
    ("a", "DT"),
    ("flight", "NN"),
    ("ticket", "NN"),
    ("now", "RB")
]

sentence2 = [
    ("This", "DT"),
    ("book", "NN"),
    ("is", "VBZ"),
    ("interesting", "JJ")
]

print("Sentence 1:")
for word, tag in sentence1:
    print(word, "/", tag)

print("\nSentence 2:")
for word, tag in sentence2:
    print(word, "/", tag)

# Q2: HMM probability

p_book_given_vb = 0.6
p_start_vb = 0.5

p_book_given_nn = 0.4
p_start_nn = 0.5

vb_probability = p_start_vb * p_book_given_vb
nn_probability = p_start_nn * p_book_given_nn

print("Probability of VB =", vb_probability)
print("Probability of NN =", nn_probability)

if vb_probability > nn_probability:
    print("Prediction: book = VB")
else:
    print("Prediction: book = NN")

# Q3: Simple comparison

rule_based = {
    "Method": "Fixed rules",
    "Flexibility": "Low",
    "Ambiguity handling": "Limited"
}

hmm = {
    "Method": "Probability",
    "Flexibility": "High",
    "Ambiguity handling": "Better"
}

print("Rule-Based Tagging:")
for key, value in rule_based.items():
    print(key, ":", value)

print("\nHMM Tagging:")
for key, value in hmm.items():
    print(key, ":", value)

print("\nRecommendation: HMM")

# Q4: Simple POS-based intent detection

sentence1 = [("Book", "VB"), ("a", "DT"), ("flight", "NN")]
sentence2 = [("This", "DT"), ("book", "NN")]

if ("Book", "VB") in sentence1:
    print("Intent: Flight Booking")

if ("book", "NN") in sentence2:
    print("Intent: Book-related query")
