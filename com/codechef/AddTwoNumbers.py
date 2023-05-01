"""
https://www.codechef.com/problems/FLOW001
"""
if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
    # Read integers a and b.
        (a, b) = map(int, input().split(' '))
        ans = a + b
        print(ans)
