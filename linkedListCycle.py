# Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p = head
        q = head.next
        while( p and q and q.next):
            if p.next == q.next:
                return True
            p, q = p.next, q.next.next
        return False
