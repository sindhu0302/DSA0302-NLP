sentence = input("Enter dialog: ")

if "?" in sentence:
    act = "Question"
elif sentence.lower().startswith(("hi", "hello")):
    act = "Greeting"
elif sentence.lower().startswith(("thanks", "thank")):
    act = "Thanking"
else:
    act = "Statement"

print("Dialog Act:", act)
