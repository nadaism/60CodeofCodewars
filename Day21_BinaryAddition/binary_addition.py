"""
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))
"""

def add_binary(a,b):
    jumlah_desimal = a + b
    
    binary = bin(jumlah_desimal)[2:]
    return binary