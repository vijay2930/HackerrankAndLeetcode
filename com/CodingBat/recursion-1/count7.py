"""
https://codingbat.com/prob/p101409
"""


def count7(n):
    if not n:
        return n
    count = (0, 1)[n % 10 == 7]
    return count + count7(n // 10)


print(count7(717))
