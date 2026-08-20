# Exercise 23: Countdown
# Print numbers from 10 to 1
# Then print "Time's up!"
# Your code here:
# Method 1
numbers = list(range(1,11))
numbers.sort(reverse=True)
for number in numbers:
    print(number)
print("Time's up")

# Method 2
for number in range(10,0,-1):
    print(number)