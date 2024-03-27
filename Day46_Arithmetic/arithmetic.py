"""
Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.
"""

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b