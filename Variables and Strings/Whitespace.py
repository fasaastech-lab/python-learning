# Exercise 5: Whitespace Cleanup
# Fix this messy input:
messy_name = "  abdulraheem   fasasi  "
# Remove all whitespace and print in title case
# Your code here:
clean_name = " ".join(messy_name.split())
print(clean_name.title())
