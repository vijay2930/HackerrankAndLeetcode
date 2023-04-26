"""
https://codingbat.com/prob/p194781
"""


def triangle(rows):
    if rows == 0 or rows == 1:
        return rows
    return rows + triangle(rows - 1)


print(triangle(4))
