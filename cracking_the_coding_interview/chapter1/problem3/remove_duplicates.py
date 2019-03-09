"""
Problem 1.3: Design an algorithm and write code to remove the duplicate characters in a
string without any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.
"""


def remove_duplicates(string):
    """
    This function keeps the first instance of a character in a string and removes all other repeats.
    Time = O(N**2).

    :param string: input string
    :return: string without duplicate characters
    """
    n = len(string)

    for i in range(n - 1, -1, -1):  # reverse string i=[n-1,n-2,...2,1,0]
        if string[i] in string[:i]:
            # if a duplicate is found, remove it from string
            string = string[:i] + string[i + 1:]

    return string
