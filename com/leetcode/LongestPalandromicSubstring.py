"""
https://leetcode.com/problems/longest-palindromic-substring/
"""

class Solution:
    def isPalindrome(self, s):
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True


    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = len(s)
        string = ""
        while start < end:
            if self.isPalindrome(s[start:end]):
                if len(string) < len(s[start:end]):
                    string = s[start:end]
                elif len(string)>start-end:
                    return string
            end -= 1
            if start + 1 == end:
                end = len(s)
                start += 1
        return string