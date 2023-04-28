"""
https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
"""


def count_substring(string, sub_string):
    count = 0
    start = 0
    end = len(sub_string)
    while end <= len(string):
        if string[start:end] == sub_string:
            count += 1
        start += 1
        end += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
