# EX06 — Functions
# Write a function clamp_rating(x) that returns:
# 1 if x < 1, 5 if x > 5, otherwise x.
# Read one integer from input, apply clamp_rating, and print the result.

def clamp_rating(x):
    if x < 1:
        return 1
    elif x > 5:
        return 5
    else:
        return x

value = int(input("Enter a number: "))
print(clamp_rating(value))
