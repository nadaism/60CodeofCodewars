"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.
"""

def sum_array(arr):
    #your code here
    if arr is None or len(arr) <= 2:
        return 0
    
    sort_arr = sorted(arr)
    return sum(sort_arr[1:-1])
    