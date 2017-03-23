# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#
# You should return [1, 3, 4].
# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:    return []
        st = [(root, 0)]
        res = []
        while(st):
            n, l = st.pop()
            if len(res) < l + 1:
                res += [n.val]
            else:
                res[l] = n.val
            if n.right: st += [(n.right, l + 1)]
            if n.left:  st += [(n.left, l + 1)]
        return res
