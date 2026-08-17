# Exercise 36: Number Type
# num = 7
# Check and print if it's:
# - Positive, Negative, or Zero
# - Even or Odd
# Your code here:
num = 7
# Checking sign
if num > 0:
    sign = 'Positive'
elif num < 0:
    sign = 'Negative'
else:
    sign = 'Zero'

# Checking Parity
if num % 2 == 0:
    parity = 'Even'
else:
    parity = 'Odd'

print(f"Number is {sign} and {parity}")