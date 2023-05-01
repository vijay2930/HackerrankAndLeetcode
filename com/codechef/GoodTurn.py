"""
https://www.codechef.com/problems/GDTURN
"""
if __name__ == "__main__":
    n = int(input())
    dice = list(list(map(int, input().split())) for i in range(n))
    for roll in dice:
        sum = roll[0] + roll[1]
        if sum > 6:
            print("YES")
        else:
            print("NO")
