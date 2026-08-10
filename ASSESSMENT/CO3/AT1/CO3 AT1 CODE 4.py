dictionary = {"the": "DT", "student": "NN", "is": "VBZ"}
sentence = ["the", "student", "is", "studying"]
# 1. Rule-Based Tagger
tags_rule = [dictionary.get(w, "NN") for w in sentence]
print("Rule-Based output:        ", tags_rule)
# 2. Stochastic Approximation Tagger
tags_stochastic = ["DT", "NN", "VBZ", "VBG"]  # Based on context odds
print("Stochastic-Inspired output:", tags_stochastic)
# 3. Transformation Tagger (Fixes the mistake in rule-based)
tags_transform = list(tags_rule)
for i in range(len(tags_transform)):
    if tags_transform[i - 1] == "VBZ" and sentence[i].endswith("ing"):
        tags_transform[i] = "VBG"  # Correcting NN to VBG
print("Transformation-Based output:", tags_transform)
