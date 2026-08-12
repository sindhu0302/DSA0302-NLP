# Q1: MLE of P(science | data)

count_data_science = 3
count_data = 3

probability = count_data_science / count_data

print("P(science | data) =", probability)
print("Percentage =", probability * 100, "%")

# Q2: Backoff for "data science improves"

# Trigram is unseen
trigram_probability = 0

# Bigram "science improves" is also unseen
bigram_probability = 0

# "improves" is not present in the corpus
unigram_probability = 0

# Backoff: Trigram -> Bigram -> Unigram
if trigram_probability > 0:
    probability = trigram_probability
elif bigram_probability > 0:
    probability = bigram_probability
else:
    probability = unigram_probability

print("Probability of 'data science improves' =", probability)

# Q3: Deleted Interpolation

lambda1 = 0.5   # Trigram
lambda2 = 0.3   # Bigram
lambda3 = 0.2   # Unigram

trigram = 2 / 3
bigram = 2 / 3
unigram = 2 / 12

probability = (
    lambda1 * trigram +
    lambda2 * bigram +
    lambda3 * unigram
)

print("Trigram probability =", trigram)
print("Bigram probability =", bigram)
print("Unigram probability =", unigram)

print("Interpolated probability =", round(probability, 3))
print("Percentage =", round(probability * 100, 2), "%")

# Q4: Entropy

import math

p_is = 0.66
p_drives = 0.33

entropy = -(p_is * math.log2(p_is) +
            p_drives * math.log2(p_drives))

print("Entropy =", round(entropy, 3), "bits")
