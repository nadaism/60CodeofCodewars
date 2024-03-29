"""
Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

Note: Notes:

If either input is an empty string, consider it as zero.

Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)

"""

def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0

    hasil = str(a + b)
    return hasil