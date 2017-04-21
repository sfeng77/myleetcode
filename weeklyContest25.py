#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Solution():
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        from math import sqrt
        divisors = set([1])
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num/i)
        # print divisors
        return num == sum(divisors)

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, ai = self.strToComp(a)
        br, bi = self.strToComp(b)
        sr = ar * br - ai * bi
        si = ar * bi + ai * br
        return str(sr) + "+" + str(si) + "i"

    def strToComp(self, s):
        a, b = s.split("+")
        return (int(a), int(b[:-1]))

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if (root.left is None) and (root.right is None):
            return [root.val]

        if (root.left is None):
            l, v, r = self.boundary(root.right)
            print v, r
            return [root.val] + v[:-1] + r

        if (root.right) is None:
            l, v, r = self.boundary(root.left)
            return [root.val] + l[:-1] + v

        l, v, r = self.boundary(root)
        return l[:-1] + v[:-1] + r[:-1]

    def boundary(self, root):
        if root is None:
            return ([], [], [])
        if (root.left is None) and (root.right is None):
            return ([root.val], [root.val], [root.val])
        if (root.left is None):
            rl, rv, rr = self.boundary(root.right)
            return ([root.val] + rl, rv, rr + [root.val])
        if (root.right is None):
            ll, lv, lr = self.boundary(root.left)
            return ([root.val] + ll, lv, lr + [root.val])

        ll, lv, lr = self.boundary(root.left)
        rl, rv, rr = self.boundary(root.right)
        return ([root.val] + ll, lv + rv, rr + [root.val])

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        pass
