"""
https://www.codechef.com/problems/CNTWRD
"""


def countingWords(pages, words):
    return pages * words


T = int(input())
test_cases = [map(int, input().split(" ")) for _ in range(T)]

for pages, words in test_cases:
    print(countingWords(pages, words))
