"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
"""


def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    letters = []
    for i in range(size):
        s = '-'.join(alpha[i:size])
        letters.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))

    print('\n'.join(letters[:0:-1] + letters))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
