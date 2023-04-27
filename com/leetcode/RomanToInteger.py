"""
https://leetcode.com/problems/roman-to-integer/
"""

def roman_to_int(s: str) -> int:

    roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for c in s[::-1]:
        curr_value = roman_to_int_dict[c]
        if curr_value < prev_value:
            result -= curr_value
        else:
            result += curr_value
        prev_value = curr_value
    return result
