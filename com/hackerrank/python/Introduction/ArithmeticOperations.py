"""
https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen
=true
"""


def arithmetic_operations(a, b):
    print(a + b)
    print(a - b)
    print(a * b)


if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    arithmetic_operations(a, b)
