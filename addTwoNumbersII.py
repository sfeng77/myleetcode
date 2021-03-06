#  You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0
        n2 = 0
        p = l1
        while(p):
            n1 = n1 * 10 + p.val
            p = p.next
        p = l2
        while(p):
            n2 = n2 * 10 + p.val
            p = p.next
        n1 = n1 + n2
        dummy = ListNode(0)
        if n1 == 0: return dummy
        while(n1):
            n1, v = n1 / 10, n1 % 10
            newNode = ListNode(v)
            p = dummy.next
            dummy.next = newNode
            newNode.next = p
        return dummy.next
