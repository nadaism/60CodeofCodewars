""" 
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(s):
    # The function code should be here
    karakter = {}
    for char in s:
        if char in karakter:
            karakter[char] += 1
        else:
            karakter[char] = 1
    return karakter
