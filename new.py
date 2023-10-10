# Import statements should be at the top of the file.
import random
import os
import sys


# Function and variable names should be lowercase with words separated by underscores.
def generate_random_number():
    return random.randint(1, 100)

# Use 4 spaces for indentation (no tabs).
if __name__ == "__main__":
    number = generate_random_number()
    print(f"Generated random number: {number}")

