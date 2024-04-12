"""
Example 1:

Input: s = "abcadbcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def find_longest_repeating_substring(string: str) -> str:
    """
    How does my algorithm work?
    string: "abcabcbb"
    hashmap_1: Substrings and their length (if equal, return first)
    hashmap_2: Ordered, will keep the order of the current word.
    Keep current highest notable and create new list with only current highest.
    :param string: String from which to search.
    :return: Longest substring without repeating chars.
    """
    highest_substring: str = ""
    symbols: dict[str, int] = {}
    for index, letter in enumerate(string):
        if letter in symbols:
            new_word: str = "".join([symbol for symbol in symbols])
            if len(new_word) > len(highest_substring):
                highest_substring = new_word
            symbols.pop(letter)
        symbols[letter] = index
    return highest_substring

print(find_longest_repeating_substring("pwwkew"))