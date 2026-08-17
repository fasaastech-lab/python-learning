# Exercise 29: Nested Loop - Grid
# Print a 4x4 grid of asterisks:
# * * * *
# * * * *
# * * * *
# * * * *
# Your code here:
asterisks = '*'*4
for asterisk in asterisks:
    for asterisk in asterisks:
        print(asterisk, end=" ")
    print()
