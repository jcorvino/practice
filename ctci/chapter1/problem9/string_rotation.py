"""
Problem 1.9: Given 2 substrings (s1 and s2) check whether s2 is a rotation of s1 given only 1 call to "in".
"""


def string_rotation(s1, s2):
    """
    Check whether s2 is a rotation of s1.
    Time complexity = O(N)?

    :param s1: string 1
    :param s2: string 2
    :return bool: True if s2 is a rotation of s1
    """
    if len(s1) == len(s2):
        return s2 in ''.join([s1, s1])
