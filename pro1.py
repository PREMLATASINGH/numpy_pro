import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
# 6. Plotting the distribution of rolls
plt.bar(unique, counts, color='blue', alpha=0.7)    
plt.xlabel('Dice Value')
plt.ylabel('Frequency')
plt.title('Distribution of 1000 Dice Rolls')
plt.xticks(unique)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), color='orange', edgecolor='black')
plt.xlabel('Dice Value')
plt.ylabel('Frequency')
plt.title('Histogram of 1000 Dice Rolls')
plt.xticks(unique)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
plt.boxplot(rolls, vert=False)
plt.title('Box Plot of Dice Rolls')
plt.xlabel('Dice Value')
plt.show()
plt.pie(counts, labels=unique, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'yellow', 'cyan', 'magenta'])
plt.title('Percentage Distribution of Dice Rolls')
plt.show()
sns.countplot(x=rolls, palette='Set2')
plt.xlabel('Dice Value')
plt.ylabel('Frequency')
plt.title('Count Plot of 1000 Dice Rolls')
plt.show()
sns.histplot(rolls, bins=np.arange(0.5, 7.5, 1), kde=True, color='purple')
plt.xlabel('Dice Value')
plt.ylabel('Frequency')
plt.title('Histogram with KDE of 1000 Dice Rolls')
plt.xticks(unique)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
print("\nSummary of Dice Rolls:")
print(f"Total Rolls: {len(rolls)}")
print(f"Average Roll: {np.mean(rolls):.2f}")
print(f"Most Frequent Roll: {unique[np.argmax(counts)]} (Count: {np.max(counts)})")
