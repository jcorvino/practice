"""
Problem 1.4 (4th ed.): Write a method to decide if two strings are anagrams or not.
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
    # Special case if first is empty string
    if first == '':
        # swap first and second so for loop executes properly
        first = second
        second = ''

    for c in first:
        if c in ignore:
            pass
        elif first.count(c) != second.count(c):
            return False
    return True
