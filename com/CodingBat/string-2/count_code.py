"""
https://codingbat.com/prob/p186048
"""


def count_code(str):
    c, o, e = 0, 1, 3
    count = 0
    while e < len(str):
        if str[c] == 'c' and str[o] == 'o' and str[e] == 'e':
            count += 1
        c, o, e = c + 1, o + 1, e + 1
    return count
