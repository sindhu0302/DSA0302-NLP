# Top-Down vs Earley Parsing

sentence = "Book a flight to Delhi"

print("Input:", sentence)

print("\nTop-Down Parsing:")
print("- Starts from the start symbol")
print("- Predicts grammar rules")
print("- May require backtracking")
print("- Less suitable for incomplete input")

print("\nEarley Parsing:")
print("- Uses dynamic programming")
print("- Handles incomplete sentences")
print("- Handles ambiguous sentences")
print("- Avoids repeated parsing")

# Simple comparison
top_down = 8
earley = 4

print("\nParsing Time:")
print("Top-Down:", top_down, "ms")
print("Earley:", earley, "ms")

if earley < top_down:
    print("\nEarley parsing is more suitable for dynamic input.")
