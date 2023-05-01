"""
https://www.codingninjas.com/codestudio/problem-of-the-day/moderate
"""
from os import *
from sys import *
from collections import *
from math import *

#    List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.pos = []

    def __del__(self):
        if (self.next):
            del self.next


def firstNode(head):
    #    Write your code here
    #    Return the node where the cycle begins
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            break
    if not fast or not fast.next:
            return None
    slow = head
    while slow !=fast:
        slow=slow.next
        fast=fast.next

    return slow
