### utility function to construct a linked list from list

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def constructList(l):
    h = ListNode(0)
    p = h
    while(l):
        p.next = ListNode(l.pop(0))
        p = p.next
    p.next = None
    return h.next

def printList(h):
    q = h
    while(q):
        print q.val, q.next
        q = q.next
