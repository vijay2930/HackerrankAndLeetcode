"""
https://codingbat.com/prob/p137918
"""


def parenBit(str):
    if str[0] != '(':
        return parenBit(str[1:])
    elif str[-1] != ')':
        return parenBit(str[:-1])
    else:
        return str
