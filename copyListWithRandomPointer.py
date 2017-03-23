# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:    return None
        myhead = RandomListNode(head.label)
        dic = {}
        dic[head] = myhead
        p = head.next
        while(p):
            print p.label
            newNode = RandomListNode(p.label)
            dic[p] = newNode
            p = p.next

        p = head
        while(p):
            print p.label
            if p.next:
                dic[p].next = dic[p.next]
            else:
                dic[p].next = None
            if p.random:
                dic[p].random = dic[p.random]
            else:
                dic[p].random = None

            p = p.next

        return myhead
