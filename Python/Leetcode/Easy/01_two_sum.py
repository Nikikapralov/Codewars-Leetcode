"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Solution:
    Look up table.
    For each num, check if its complimentary required for the target sum is in the lookup table.
    If yes, return it, otherwise continue.
    Complexity O(N).
    Space O(N) because we need a lookup table.
    :param numbers: List of numbers.
    :param target: The target sum.
    :return: The indexes of the two numbers that create the sum.
    """
    lookup_dictionary: dict[int, int] = {}
    for index, number in enumerate(numbers):
        complementary: int = target - number
        complementary_index: int = lookup_dictionary.get(complementary, None)
        if complementary_index is not None:
            return [index, complementary_index]
        lookup_dictionary[number] = index

print(two_sum([2,7,11,15], 9))