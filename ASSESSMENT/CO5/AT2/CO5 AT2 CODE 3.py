conversation = [
    ("User", "Can you book a train ticket for me?", "Request"),
    ("Agent", "Sure, where would you like to travel?", "Question"),
    ("User", "I want to go to Chennai.", "Inform"),
    ("Agent", "Your ticket has been booked.", "Confirmation")
]

print("Dialogue Act Classification:\n")

for speaker, utterance, act in conversation:
    print(speaker, ":", utterance)
    print("Dialogue Act:", act)
    print()

print("Dialogue Act Sequence:")
print("Request -> Question -> Inform -> Confirmation")
