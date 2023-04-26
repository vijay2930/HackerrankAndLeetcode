"""
https://codingbat.com/prob/p186177
"""


def strCount(s, sub):
    if not s:
        return 0
    count = (0, 1)[s[:len(sub)] == sub]
    return count+strCount(s[1:],sub)

print(strCount("catcowcat","dog"))
