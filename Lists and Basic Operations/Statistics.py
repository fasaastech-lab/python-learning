# Exercise 15: List Statistics
# scores = [78, 92, 85, 88, 76, 94, 81]
# Find and print:
# - Highest score
# - Lowest score
# - Average score
# - Number of scores
# Your code here:
scores = [78, 92, 85, 88, 76, 94, 81]
# - Highest score
print('Highest score:',max(scores))
# - Lowest score
print('Lowest score:',min(scores))
# - Average score
Average_score = sum(scores)/len(scores)
print('Average score:',round(Average_score, 2))
# - Number of scores
print('Number of scores:',len(scores))