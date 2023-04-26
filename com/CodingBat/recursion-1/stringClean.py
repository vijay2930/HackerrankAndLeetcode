"""
https://codingbat.com/prob/p104029
"""


def stringClean(s):
    if len(s) < 2:
        return s
    s = (s[0], "")[s[0] == s[1]] + s[1:]
    return (s[0], "")[s[0] == s[1]]+stringClean(s[1:])


print(stringClean("hello"))
