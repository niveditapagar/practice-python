"""
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
"""


def left2(my_str):
    return f"{my_str[2:]}{my_str[:2]}" if len(my_str) > 2 else my_str
