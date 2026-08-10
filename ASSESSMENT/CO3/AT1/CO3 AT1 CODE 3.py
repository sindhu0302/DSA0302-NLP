import math
# Unsmoothed vs Smoothed probabilities
prob_seen = 0.5
prob_unseen_unsmoothed = 0.0
prob_unseen_smoothed = 0.05
print("--- Entropy (Uncertainty) Score ---")
# 1. Predictable seen phrase
entropy_seen = -math.log2(prob_seen)
print(f"Seen phrase uncertainty: {entropy_seen:.2f} bits")
# 2. Unseen phrase under Unsmoothed model
print("Unseen phrase (Unsmoothed): Crash! Cannot compute log(0)")
# 3. Unseen phrase under Smoothed model
entropy_smoothed = -math.log2(prob_unseen_smoothed)
print(f"Unseen phrase (Smoothed): {entropy_smoothed:.2f} bits")
