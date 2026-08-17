# Exercise 40: Comparison Chain
# test_score = 85
# Check against three thresholds:
# - Excellence: 90+
# - Merit: 80-89
# - Pass: 50-79
# - Fail: <50
# Print appropriate message
# Your code here:
test_score = 85
if test_score >= 90:
    print("Excellence")
elif test_score > 79:
    print('Merit')
elif test_score > 49:
    print('Pass')
else:
    print('Fail')
    