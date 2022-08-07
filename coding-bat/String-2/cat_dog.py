"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""


def cat_dog(my_str):
    count_dog = sum([1 for i in range(len(my_str) - 2) if my_str[i: i + 3] == "dog"])
    count_cat = sum([1 for i in range(len(my_str) - 2) if my_str[i: i + 3] == "cat"])

    return count_cat == count_dog
