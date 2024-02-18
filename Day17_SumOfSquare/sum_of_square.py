"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
"""

import math
def square_sum(numbers):
    sum_of_square = 0
    for i in numbers:
        sum_of_square += i**2
    return sum_of_square