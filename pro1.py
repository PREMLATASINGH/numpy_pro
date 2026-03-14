import numpy as np

# 1. Simulate 1000 dice rolls (values 1 to 6)
rolls = np.random.randint(1, 7, size=1000)
print("First 20 rolls:", rolls[:20])

# 2. Count frequency of each number
unique, counts = np.unique(rolls, return_counts=True)
frequency = dict(zip(unique, counts))
print("\nFrequency of each number:", frequency)

# 3. Calculate probability of each outcome
probabilities = counts / len(rolls)
print("\nEstimated probabilities:")
for num, prob in zip(unique, probabilities):
    print(f"{num}: {prob:.3f}")

# 4. Basic statistics
print("\nAverage roll value:", np.mean(rolls))
print("Most frequent number:", unique[np.argmax(counts)])
print("Least frequent number:", unique[np.argmin(counts)])

# 5. Extra: difference between consecutive rolls
diffs = np.diff(rolls)
print("\nDifference between consecutive rolls (first 20):", diffs[:20])