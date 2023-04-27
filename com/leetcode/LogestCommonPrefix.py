"""
https://leetcode.com/problems/longest-common-prefix/editorial/
"""

def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ''
    shortest_str = min(strs, key=len)
    for i, c in enumerate(shortest_str):
        for other_str in strs:
            if other_str[i] != c:
                return shortest_str[:i]
    return shortest_str
