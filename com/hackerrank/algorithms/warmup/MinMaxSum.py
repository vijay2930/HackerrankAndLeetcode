"""
https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
"""

def miniMaxSum(arr):
    max=float('-inf')
    min=float('inf')
    sum=0
    for val in arr:
        sum+=val
        if max<val:
            max=val
        if min>val:
            min=val
    return sum-max,sum-min
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
