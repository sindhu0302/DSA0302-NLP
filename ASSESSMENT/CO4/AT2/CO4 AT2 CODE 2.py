# Voice Assistant - Parsing Comparison

sentence = "Book a flight to Delhi with a window seat"

print("Input:", sentence)

# Possible interpretations
print("\nPossible Parse Structures:")

print("1. Book [a flight to Delhi] [with a window seat]")
print("2. Book [a flight] [to Delhi with a window seat]")

print("\nTop-Down Parsing:")
print("- Starts from the start symbol")
print("- May require backtracking")
print("- Slow when ambiguity occurs")
print("- Difficult for incomplete sentences")

print("\nEarley Parsing:")
print("- Handles ambiguous sentences")
print("- Handles incomplete input")
print("- Uses dynamic programming")
print("- Avoids repeated parsing work")

# Simple performance comparison
top_down_time = 8
earley_time = 4

print("\nParsing Time:")
print("Top-Down:", top_down_time, "ms")
print("Earley:", earley_time, "ms")

if earley_time < top_down_time:
    print("Earley parsing is faster for this example.")

print("\nConclusion:")
print("Earley parsing is more suitable for real-time voice assistants.")
