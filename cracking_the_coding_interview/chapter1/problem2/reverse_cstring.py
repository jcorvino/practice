"""
Problem 1.2: Write code to reverse a C-Style string.
C-Style means that "abcd" is represented as 5 characters, including the null character.
"""


def reverse_cstring(s):
    """
    Reverses order of C-Style string (string with ending null character)
    Time = O(n).

    :param s: C-Style string
    :return: reversed string
    """
    try:
        # Note: Assumed C-String null character is a single character (len(null_char)=1)
        null_char = s[-1]
    except IndexError:
        raise Exception(f'Error: Input string {s} does not have a null character. Must be C-Style.')
    return s[-2::-1] + null_char
