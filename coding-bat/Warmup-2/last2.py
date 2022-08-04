"""
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as
the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""


def last2(my_str):
    if len(my_str) < 3:
        return 0

    return sum([1 if my_str[-2:len(my_str)] == my_str[i:i+2] else 0 for i in range(len(my_str) - 2)])
