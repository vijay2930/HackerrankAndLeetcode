"""
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
"""

def diagonalDifference(arr):
    left = -1
    right = len(arr)
    left_sum = right_sum = 0
    for i in range(len(arr)):
        left_sum += arr[i][left := left + 1]
        right_sum += arr[i][right := right - 1]
    return abs(left_sum - right_sum)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
