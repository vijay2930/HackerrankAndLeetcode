"""
https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
"""


def if_else(n):
    if n % 2 == 1 or (n % 2 == 0 and 6 <= n <= 20):
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    else:
        print("Not Weird")


if __name__ == "__main__":
    n = int(input("Enter n: "))
    if_else(n)
