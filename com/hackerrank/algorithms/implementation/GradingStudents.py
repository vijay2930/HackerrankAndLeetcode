"""
https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
"""


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38 and grades[i] % 5 >= 3:
            grades[i] = grades[i] + (5 - grades[i] % 5)
    return grades


if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
