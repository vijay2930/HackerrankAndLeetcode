"""
https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
"""


def plusMinus(arr):
    postive = 0
    negative = 0
    zero = 0
    length = len(arr)
    for val in arr:
        if val > 0:
            postive += 1
        elif val < 0:
            negative += 1
        else:
            zero += 1
    return postive / length, negative / length, zero / length


if __name__ == '__main__':
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        plusMinus(arr)
