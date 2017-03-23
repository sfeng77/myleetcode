# Given preorder and inorder traversal of a tree, construct the binary tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        dic = {}
        n = len(inorder)
        for i in range(n):
            dic[inorder[i]] = i

        if n == 0:  return None
        root = TreeNode(preorder[0])
        st = [(root,0,n-1,0,n-1)]
        while(st):
            n, a, b, c, d = st.pop()
            n.val = preorder[c]
            i = dic[n.val]
            if i > a:
                n.left = TreeNode(0)
                st += [(n.left, a, i-1, c + 1, c + (i-a) -1)]
            if b > i:
                n.right = TreeNode(0)
                st += [(n.right, i + 1, b, c + (i-a), d)]
        return root
