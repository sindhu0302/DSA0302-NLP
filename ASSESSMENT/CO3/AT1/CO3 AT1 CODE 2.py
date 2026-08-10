# Setup basic frequencies
words = "the student is studying the student is writing".split()
total_words = len(words)
c_student_is = 2
c_is = 2
# 1. Backoff strategy
def smart_backoff(w1, w2, w3):
    # Try looking for full 3-word phrase first, then fall back
    if w1 == "student" and w2 == "is" and w3 == "studying":
        return 1.0
    elif w2 == "is" and w3 == "smart":  # Unseen trigram, fallback to bigram
        return 0.4 * (c_is / total_words)
    return 0.01  # Safe floor value
# 2. Interpolation strategy
def interpolate(w3):
    p3 = 0.0  # 3-gram probability (unseen)
    p2 = c_is / total_words  # 2-gram probability
    p1 = words.count(w3) / total_words  # 1-gram probability
    return (0.5 * p3) + (0.3 * p2) + (0.2 * p1)
print("Backoff prob for 'student is smart':", smart_backoff("student", "is", "smart"))
print("Interpolation prob for 'smart':", interpolate("smart"))
