"""
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""


def count_hi(my_str):
    return sum([1 for i in range(len(my_str) - 1) if my_str[i: i + 2] == "hi"])
