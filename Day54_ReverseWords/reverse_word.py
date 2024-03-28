"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
"""

def reverse_words(text):
  #go for it
    kata = text.split(" ")
    reversed_words = [word[::-1] for word in kata]
    return " ".join(reversed_words)
    