"""
https://codingbat.com/prob/p192383
"""


def count8(n):
    if not n:
        return n
    count = (0, 1)[n % 10 == 8]
    count += count and (0, 1)[(n // 10) % 10 == 8]
    return count + count8(n // 10)


print(count8(88188))
