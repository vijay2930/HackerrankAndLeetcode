"""
https://www.codechef.com/problems/APPLORNG
"""
import sys


def applesAndOranges(amount, apple, orange):
    return ("NO", "YES")[apple + orange <= amount]


amount = int(sys.stdin.readline())
apple, orange = map(int, sys.stdin.readline().split(" "))

sys.stdout.write(str(applesAndOranges(amount, apple, orange)))
