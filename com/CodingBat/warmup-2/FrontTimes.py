"""
https://codingbat.com/prob/p165097
"""
def front_times(str, n):
    return str[:min(len(str),3)]*n
