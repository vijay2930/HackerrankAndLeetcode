"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_length = 0
        for end in range(len(s)):
            if s[end] in seen and seen[s[end]] >= start:
                start = seen[s[end]] + 1
            seen[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length


if __name__=="__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))