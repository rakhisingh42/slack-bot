# Import statements should be at the top of the file.
import random
import os
import sys


def add_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their sum.
    
    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.
    
    Returns:
        int or float: The sum of num1 and num2.
    """
    result = num1 + num2
    return result

# Example usage:
num1 = 5
num2 = 3
sum_result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {sum_result}")


