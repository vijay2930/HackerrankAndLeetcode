"""
https://codingbat.com/prob/p124806
"""


def make_ends(nums):
    res=[]
    if(nums==1):
        res=nums
    else:
        res=[nums[0],nums[-1]]
    return res