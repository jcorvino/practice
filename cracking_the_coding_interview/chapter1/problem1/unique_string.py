"""
Problem 1.1: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique_1(string):
    """
    Checks if all characters in a string are unique. Uses a simple algorithm to count occurrences of each character.
    Time = O(n**2). Space = O(1).

    :param string: a string
    :return: True if unique. False otherwise.
    """
    for s in string:
        if string.count(s) > 1:
            return False
    return True


def is_unique_2(string):
    """
    Checks if all characters in a string are unique.
    Uses a list of True/False to check which unicode character has appeared.
    Time = O(n). Space = O(1).

    :param string: a string
    :return: True if unique. False otherwise.
    """
    characters = [False] * 110001  # List of True/False for each unicode character (0x110000)
    for s in string:
        i = ord(s)
        if characters[i]:
            return False
        characters[i] = True
    return True
