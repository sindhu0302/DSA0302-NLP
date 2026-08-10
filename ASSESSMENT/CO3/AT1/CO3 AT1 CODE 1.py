text = "the student is studying hard the student is writing an essay"
words = text.split()
# Count occurrences
unigrams = {w: words.count(w) for w in set(words)}
bigrams = {
    (words[i], words[i + 1]): words.count(words[i] + " " + words[i + 1])
    for i in range(len(words) - 1)
}
# 1. Predict next word using Bigram (N=2)
context = "student"
next_word_counts = {
    w: words.count("student " + w) for w in set(words) if "student " + w in text
}
print("Predictions for 'student':", next_word_counts)
# 2. Unseen sequence error demonstration
unseen_count = words.count("student is cooking")
print("Probability of 'student is cooking':", unseen_count)
