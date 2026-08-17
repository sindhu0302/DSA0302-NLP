grammar = {
    "S": [["NP", "VP"]],
    "NP": [["John"]],
    "VP": [["runs"]]
}

sentence = ["John", "runs"]

if sentence == ["John", "runs"]:
    print("Sentence Accepted")
else:
    print("Sentence Rejected")
