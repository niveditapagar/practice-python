"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky,
so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""


def sum13(nums):
    new_array = []
    if 13 in nums:
        new_array.append(nums[0] if nums[0] != 13 else 0)
        for i in range(1, len(nums)):
            if nums[i] == 13 or nums[i - 1] == 13:
                continue
            new_array.append(nums[i])
    return sum(nums) if 13 not in nums else sum(new_array)
