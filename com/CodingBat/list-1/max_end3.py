"""
https://codingbat.com/prob/p135290
"""

def max_end3(nums):
    largest=nums[0] if(nums[0]>nums[-1]) else nums[-1]
    return [largest]*3