"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without 
any elements with the same value next to each other and preserving the original order of elements.
"""

def unique_in_order(sequence):
    unik = []
    prev = None
    for item in sequence:
        if item != prev:
            unik.append(item)
            prev = item
    return unik
