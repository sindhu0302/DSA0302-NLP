# Banking Chatbot - Simple CFG Analysis

sentence = "Show me the transactions with the card from last month"

# Possible interpretations
parse1 = "Transactions FROM last month"
parse2 = "Transactions WITH the card"

print("Input:", sentence)

print("\nPossible CFG Interpretations:")
print("1.", parse1)
print("2.", parse2)

print("\nProblem:")
print("CFG cannot easily decide which phrase is the correct interpretation.")

# Simple improved approach
print("\nImproved Method: PCFG + Feature Structures + Earley Parsing")

probability1 = 0.70
probability2 = 0.30

if probability1 > probability2:
    print("Selected interpretation:", parse1)
else:
    print("Selected interpretation:", parse2)

print("\nFeature Check:")
subject = "customer"
verb = "show"

if subject == "customer" and verb == "show":
    print("Subject-verb agreement: Correct")

print("\nAdvantages:")
print("- PCFG selects the most probable interpretation")
print("- Feature structures handle agreement")
print("- Earley parsing handles long and ambiguous queries")
print("- Faster and more accurate chatbot responses")
