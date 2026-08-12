# Q1: Apply transformation rule

words = [
    ("economic", "JJ"),
    ("growth", "NN"),
    ("increases", "NNS"),
    ("employment", "NN")
]

# Apply rule:
# Change NNS to VBZ if previous word is NN

for i in range(1, len(words)):
    current_word, current_tag = words[i]
    previous_word, previous_tag = words[i - 1]

    if current_tag == "NNS" and previous_tag == "NN":
        words[i] = (current_word, "VBZ")

print("Corrected POS tags:")

for word, tag in words:
    print(word, "/", tag)

# Q2: Check whether the tag is correct

word = "increases"
initial_tag = "NNS"
previous_tag = "NN"

if initial_tag == "NNS" and previous_tag == "NN":
    corrected_tag = "VBZ"
else:
    corrected_tag = initial_tag

print("Word:", word)
print("Initial tag:", initial_tag)
print("Corrected tag:", corrected_tag)

# Q3: Word frequency distribution

frequency = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

total = sum(frequency.values())

print("Total frequency =", total)
print("\nWord probabilities:")

for word, count in frequency.items():
    probability = count / total
    print(word, "=", round(probability, 3))

# Q4: Entropy before and after transformation

import math

# Before rule: uncertain between NNS and VBZ
p_nns = 0.5
p_vbz = 0.5

entropy_before = -(p_nns * math.log2(p_nns) +
                   p_vbz * math.log2(p_vbz))

# After rule: VBZ is selected with full confidence
p_vbz_after = 1.0

entropy_after = -(p_vbz_after * math.log2(p_vbz_after))

print("Entropy before rule =", entropy_before, "bits")
print("Entropy after rule =", entropy_after, "bits")
