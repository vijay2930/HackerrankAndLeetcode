"""
https://codingbat.com/prob/p183174
"""


def nestParen(s):
    if not s:
        return True
    if s[0] == '(':
        return nestParen(s[1:])
    if s[-1] == ')':
        return nestParen(s[:-1])
    return False
