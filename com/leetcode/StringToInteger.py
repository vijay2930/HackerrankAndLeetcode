"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        i = 0
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        if num < -2 ** 31:
            return -2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return num
