"""
https://leetcode.com/problems/palindrome-number/
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        num = x
        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10

        return x == rev
