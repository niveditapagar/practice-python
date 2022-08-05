"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

make_pi() → [3, 1, 4]
"""
import math


def make_pi():
    # simple
    # return [3, 1, 4]

    # using math.pi
    return [int(element) for element in str(math.pi)[0:4] if element != "."]
