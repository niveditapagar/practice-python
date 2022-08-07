"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a
period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""


def xyz_there(my_str):
    return any(["xyz" for i in range(len(my_str) - 2) if my_str[i: i + 3] == "xyz" and my_str[i - 1] != "."])
