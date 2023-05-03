"""
https://www.codechef.com/problems/SPECIALITY
"""


def speciality(x, y, z):
    if y < x and z < x:
        return "Setter"
    if x < y and z < y:
        return "Tester"
    else:
        return "Editorialist"


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y, z in testCase:
    print(speciality(x, y, z))
