"""
https://codingbat.com/prob/p149391
"""


def xyz_there(str):
    for i in range(len(str)):
        is_dot=False
        if str[i-1]=='.':
            is_dot=True
        if str[i:i+3]=="xyz" and not is_dot:
            return True
    else:
        return False