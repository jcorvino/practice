"""
Problem 1.4: Write a method to decide if two strings are anagrams or not.
"""


def is_anagram(first, second, ignore=''):
    """
    Compares 2 strings to determine if they are anagrams (option to ignore specific characters such as space).
    Time = O(N**2).

    :param first: string 1
    :param second: string 2
    :param ignore: string of all characters to ignore
    :return: True if anagram, False otherwise
    """
    for c in first:
        if c in ignore:
            pass
        elif first.count(c) != second.count(c):
            return False
    return True
