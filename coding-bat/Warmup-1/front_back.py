"""
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


def front_back(my_str):
    return f"{my_str[-1]}{my_str[1:-1]}{my_str[0]}" if len(my_str) > 2 else f"{my_str[-1]}{my_str[0]}" if len(
        my_str) == 2 else my_str
