"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""


def string_splosion(my_str):
    return "".join([my_str[0:i] for i in range(len(my_str) + 1)])
