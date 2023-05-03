"""
https://www.codechef.com/problems/PRACTICEPERF
"""

p1, p2, p3, p4 = map(int, input().split(" "))


def praticeMakesUsPerfect(p1, p2, p3, p4):
    count = (0, 1)[p1 >= 10] + (0, 1)[p2 >= 10] + (0, 1)[p3 >= 10] + (0, 1)[p4 >= 10]
    return count


print(praticeMakesUsPerfect(p1, p2, p3, p4))
