"""
https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
"""
if __name__ == "__main__":
    n, m = map(int, input().split())

    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in range(n - 2, -1, -2):
        print((".|." * i).center(m, "-"))
