"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Deque uses a linked list implementation
from collections import deque


def get_number(number_ll: deque[int]) -> int:
    """
    Compute the number from the linked list.
    :param number_ll: The number where each digit is a node in the LL.
    :return: The computed number in reverse.
    """
    number_final: int = 0
    multiply: int = 1
    while number_ll:
        number: int = number_ll.popleft()
        number_final += number * multiply
        multiply *= 10
    return number_final


def add_two_numbers(number_ll_1: deque[int], number_ll_2: deque[int]) -> deque[int]:
    """
    Get the first number by iterating through the LL and then reverse it.
    Get the second number the same way.
    Sum the numbers.
    Create the result.
    :param number_ll_1: First linked list holding the number in reverse order.
    :param number_ll_2: Second linked list holding the number in reverse order.
    :return: The sum of the two numbers as a linked list, in reverse.
    """
    numbers: list[deque[int]] = [number_ll_1, number_ll_2]
    sum_result: int = 0
    final_result: deque[int] = deque([])
    for number in numbers:
        sum_result += get_number(number_ll=number)
    str_sum_result: str = str(sum_result)

    for index in range(len(str_sum_result) - 1, -1, -1):
        final_result.append(int(str_sum_result[index]))

    return final_result



print(add_two_numbers(number_ll_1=deque([2, 4, 9]), number_ll_2=deque([5, 6, 4, 9])))