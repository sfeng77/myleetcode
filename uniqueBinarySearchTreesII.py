# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from serializeTree import Codec

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        #c = Codec()

        def copyTemplate(t, nums):
            if not t:
                return None

            root = TreeNode(nums[t.val - 1])
            st1 = [t]
            st2 = [root]
            while(st1):
                n = st1.pop()
                r = st2.pop()
                if n.right:
                    r.right = TreeNode(nums[n.right.val-1])
                    st1 += [n.right]
                    st2 += [r.right]
                if n.left:
                    r.left = TreeNode(nums[n.left.val-1])
                    st1 += [n.left]
                    st2 += [r.left]
            return root

        dp = [[] for _ in range(n + 1)]
        dp[0] = [None]
        dp[1] = [TreeNode(1)]
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                for t1 in dp[j-1]:
                    for t2 in dp[i-j]:
                        t = TreeNode(j)
                        t.left = copyTemplate(t1, range(1, j))
                        t.right = copyTemplate(t2, range(j + 1, i + 2))
                        #print i,j,c.serialize(t1),c.serialize(t2),c.serialize(t)
                        dp[i] += [t]
        return dp[n]
