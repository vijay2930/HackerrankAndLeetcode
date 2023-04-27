"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
"""

if __name__ == '__main__':
    n = int(input())

    students = []

    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    students.sort(key=lambda x: x[1])

    second_lowest = sorted(set([x[1] for x in students]))[1]
    students.sort(key=lambda x: x[0])
    for name, score in students:
        if score == second_lowest:
            print(name)
