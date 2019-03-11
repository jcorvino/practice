"""
Problem 1.5: There are 3 types of edits that can be performed on a string: insert, remove, or replace.
Given 2 strings, write a function to verify if they are 1 (or 0) edits away.
"""


def one_away_1(first, second):
    """
    Function to compare if two strings are more than 1 edit away from each other.
    First attempt to solve. Too slow. Time = O(N**2) (worse case O(N**3)).

    :param first: first string
    :param second: second string
    :return: True if less than 2 edits required, False otherwise
    """
    if len(first) >= len(second):
        longer_string = first
    else:
        longer_string = second

    diffs = 0
    ignore = ''
    for char in longer_string:
        if char not in ignore:  # don't double count characters
            diffs += abs(first.count(char) - second.count(char))
            ignore += char
            if diffs > 1:
                return False

    return True


def one_away_2(first, second):
    """
    Function to compare if two strings are more than 1 edit away from each other.
    Second attempt to solve. Time = O(N)

    :param first: first string
    :param second: second string
    :return: True if less than 2 edits required, False otherwise
    """
    # Check length of strings to determine which operation is allowed
    if len(first) == len(second):
        # Only allowed 1 replace operation
        diff = False
        for i, char in enumerate(first):
            if char != second[i]:
                if diff:
                    return False
                else:
                    diff = True

    elif abs(len(first) - len(second)) == 1:
        # Only allowed 1 insert/remove operation
        if len(first) > len(second):
            shorter_string = second
            longer_string = first
        else:
            shorter_string = first
            longer_string = second

        j = 0
        for i, char in enumerate(shorter_string):
            if char != longer_string[j]:
                if i != j:
                    return False
                else:
                    j += 1
            j += 1

    else:
        # More than one away
        return False

    return True
