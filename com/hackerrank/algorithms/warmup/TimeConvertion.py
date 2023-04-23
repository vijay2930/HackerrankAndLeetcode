"""
https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
"""


def timeConversion(s):
    if s[-2:] == "PM" and s[:2] != "12":
        hour = str((int(s[:2]) + 12) % 24)
        s = f"{hour:02}" + s[2:]
    elif s[-2:] == "AM" and s[:2] == "12":
        s = "00" + s[2:]
    return s[:-2]


def timeConversion(s):
    if s[-2:] == "PM" and s[:2] != "12":
        hour = (int(s[:2]) + 12) % 24
        s = (str(hour) if hour else "00") + s[2:]
    elif s[-2:] == "AM" and s[:2] == "12":
        s = "00" + s[2:]
    return s[:-2]


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
