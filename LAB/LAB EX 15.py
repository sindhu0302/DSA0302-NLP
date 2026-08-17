rules = {
    "S -> NP VP": 0.9,
    "NP -> John": 0.5,
    "VP -> runs": 0.6
}

probability = 0.9 * 0.5 * 0.6

print("Sentence: John runs")
print("Probability:", probability)
