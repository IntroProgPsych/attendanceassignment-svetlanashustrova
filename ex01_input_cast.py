# EX01 — Input & Type Casting
# Ask the user for two values: age (integer) and hours_slept (float).
# Print: (1) age next year, and (2) whether hours_slept is at least 8.0 (True/False).

age = int(input("Enter your age: "))
hours_of_sleep = float(input("Enter how many hours did you sleep: "))

print(f"You are {age + 1} next year") 
print("Slept at lest 8 hours:", hours_of_sleep >= 8.0)