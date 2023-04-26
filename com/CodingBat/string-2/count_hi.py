"""
https://codingbat.com/prob/p167246
"""


def count_hi(str):
    count = 0
    i, j = 0, 2
    while j <= len(str):
        print(str[i:j])
        if str[i:j] == "hi":
            count += 1
        i += 1
        j += 1
    return count
