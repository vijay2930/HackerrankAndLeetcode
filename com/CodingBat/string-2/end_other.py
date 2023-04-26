"""
https://codingbat.com/prob/p174314
"""


def end_other(a, b):
    if len(a) < len(b):
        a, b = b, a
    return a[len(a) - len(b):].lower() == b.lower()
