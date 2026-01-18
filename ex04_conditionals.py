# EX04 — Conditionals
# Ask the user for an integer score from 0 to 100.
# Print "fail" for <50, "pass" for 50–79, "excellent" for 80–100, and "invalid" otherwise.

score = int(input("Please enter a score from 0 to 100: "))

if score < 0 or score > 100:
    print("invalid")
elif score < 50:
    print("fail")
elif score < 80:
    print("pass")
else:
    print("excellent")
