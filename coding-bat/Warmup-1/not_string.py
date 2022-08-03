"""
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""


def not_string(my_str):
    return my_str if len(my_str) >= 3 and my_str[:3] == "not" else f"not {my_str}"
