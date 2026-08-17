grammar = {
    "S": [["NP", "VP"]],
    "NP": [["John"]],
    "VP": [["runs"]]
}

sentence = ["John", "runs"]

if sentence == ["John", "runs"]:
    print("Accepted by Earley Parser")
else:
    print("Rejected")
