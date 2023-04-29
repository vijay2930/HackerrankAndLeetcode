"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digit_to_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            if not next_digits:
                result.append(combination)
            else:
                for letter in digit_to_letter[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        result = []
        backtrack('', digits)
        return result
