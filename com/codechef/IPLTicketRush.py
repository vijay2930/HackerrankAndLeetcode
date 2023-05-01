"""
https://www.codechef.com/problems/IPLTRSH
"""

T = int(input())
ipl_tickets = [list(map(int, input().split(" "))) for _ in range(T)]
for students, available in ipl_tickets:
    print((0, students - available)[students > available])
