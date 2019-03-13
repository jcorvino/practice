"""
Problem 1.6: Implement a method to perform basic string compression using the counts of repeated characters. If the
compressed string is longer than the original string, then return the original string. NOTE: Assume only upper/lower
case A-Z characters are allowed.
Example:
'aabcccccaaa' -> a2b1c5a3
"""


def string_compressor(string):
    """
    A function that compresses strings made up of alphabet characters.
    Time = O(N).

    :param string: string to be compressed
    :return: compressed string
    """
    previous = None
    count = 0
    compressed_list = []
    for char in string:
        if previous is None:
            count += 1
            previous = char
        elif char == previous:
            count += 1
        else:
            compressed_list.append(previous + str(count))
            count = 1
            previous = char
    compressed_list.append(previous + str(count))

    # Convert list to string
    compressed_string = ''.join(compressed_list)

    if len(compressed_string) > len(string):
        compressed_string = string

    return compressed_string
