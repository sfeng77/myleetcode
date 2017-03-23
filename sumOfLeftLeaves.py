
#Find the sum of all left leaves in a given binary tree.
#
#Example:
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
#There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = 0
        if  root.left:
            if root.left.left or root.left.right:
                sum += self.sumOfLeftLeaves(root.left)
            else:
                sum += root.left.val
        sum += self.sumOfLeftLeaves(root.right)
        return sum
