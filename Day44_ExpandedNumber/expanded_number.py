"""
You will be given a number and you will need to return it as a string in Expanded Form.

example: 
expanded_form(12) # Should return '10 + 2'
"""

def expanded_form(num):
    num_str = str(num)
    result = []
    for i, digit in enumerate(num_str):
        if digit != '0':
            result.append(digit + '0' * (len(num_str) - i - 1))
    return ' + '.join(result)
