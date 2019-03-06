"""
Problem 1.1: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(string):
    """
    Checks if all characters in a string are unique

    :param string: a string
    :return: True if unique. False otherwise.
    """
    for s in string:
        if string.count(s) > 1:
            return False
    return True



