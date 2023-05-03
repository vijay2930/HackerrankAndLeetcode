"""
https://www.codechef.com/problems/AIANALYSE
"""

def aiAnalysingCode(n):
    return ("NO", "YES")[n <= 1000]


n = int(input())
print(aiAnalysingCode(n))

