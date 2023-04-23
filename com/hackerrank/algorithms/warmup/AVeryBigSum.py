"""
https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true
"""



def aVeryBigSum(ar):
    sum = 0
    for val in ar:
        sum += val
    return sum


if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)
