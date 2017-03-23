# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
#
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:    return 0

        def sumTree(root, base):

            if (not root.left) and (not root.right):
                return base * 10 + root.val

            mysum = 0
            if root.left:
                mysum += sumTree(root.left,base * 10 + root.val)

            if root.right:
                mysum += sumTree(root.right,base * 10 + root.val)

            return mysum

        return sumTree(root, 0)
