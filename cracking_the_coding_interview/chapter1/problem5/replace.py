"""
Problem 1.5: Write a method to replace all spaces in a string with '%20'.
NOTE: I will assume the str.replace method is not available.
"""


def replace(string):
    """
    Replaces all spaces in a string with '%20' without using the str.replace method.

    :param string: input string
    :return: string with '%20' instead of spaces
    """
    n = len(string)

    for i in range(n - 1, -1, -1):  # reverse order
        if string[i] == ' ':
            string = string[:i] + '%20' + string[i + 1:]
    return string
