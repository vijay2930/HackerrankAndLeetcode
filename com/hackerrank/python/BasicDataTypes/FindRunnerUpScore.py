"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
?isFullScreen=true
"""


def second_max(arr):
    first = float('-inf')
    second = float('-inf')
    for val in arr:
        if first < val:
            second = first
            first = val
        elif second < val and first != val:
            second = val
    return second


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(second_max(arr))
