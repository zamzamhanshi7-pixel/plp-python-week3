
# Bug Hunt

count = 1
total = 0

# BUG: Added a colon because a while loop requires one.
# BUG: Changed < 5 to <= 5 to include number 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Used an f-string to print the integer total correctly.
print(f"Sum of 1 to 5 is: {total}")
