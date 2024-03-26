"""
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
"""

def sum_mix(arr):
    total_sum = 0
    for element in arr:
        if isinstance(element, str):
            total_sum += int(element)
        else:
            total_sum += element
    return total_sum