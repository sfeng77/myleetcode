"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

"""

from __linkedLists import ListNode

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        q1 = h1 = ListNode(0)
        q2 = h2 = ListNode(0)
        p = head
        while(p):
            node = p
            p = p.next
            node.next = None
            if node.val < x:
                q1.next = node
                q1 = q1.next
            else:
                q2.next = node
                q2 = q2.next
        q1.next = h2.next
        return h1.next
