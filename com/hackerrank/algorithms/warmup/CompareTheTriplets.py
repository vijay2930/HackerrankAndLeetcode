"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
"""


def compareTriplets(a, b):
    a_count = 0
    b_count = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            b_count += 1
        elif b[i]<a[i]:
            a_count += 1
    return a_count,b_count


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
