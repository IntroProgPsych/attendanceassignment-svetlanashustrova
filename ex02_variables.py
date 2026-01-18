# EX02 — Variables
# Create variables first_name (string), last_name (string), and year_of_birth (integer).
# Compute the user's approximate age as 2026 - year_of_birth and print a greeting:
# "Hello, <first_name> <last_name>. You are about <age> years old."

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
year_of_birth = int(input("Enter a year you were born: "))

age = 2026 - year_of_birth

print(f"Hello {first_name} {last_name}. You are about {age} years old.")