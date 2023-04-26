"""
https://codingbat.com/prob/p163932
"""

def sumDigits(n):
    if not n:
        return n
    return n%10+sumDigits(n//10)
print(sumDigits(126))