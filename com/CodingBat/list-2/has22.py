"""
https://codingbat.com/prob/p119308
"""

def has22(nums):
    is_two=False
    for val in nums:
        if val==2:
            if is_two:
                return True
            else:
                is_two=True
        else:
            is_two=False
    return False

