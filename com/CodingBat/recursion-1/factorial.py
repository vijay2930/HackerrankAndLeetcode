"""
https://codingbat.com/prob/p154669
"""

def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)
