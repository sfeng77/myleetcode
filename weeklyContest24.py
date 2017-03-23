#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Solution():

# Diameter of Binary Tree
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m, mmax = self.mydia(root)
        return mmax

    def mydia(self, root):
        if not root:
            return 0, 0
        l, lmax = self.mydia(root.left)
        r, rmax = self.mydia(root.right)
        m = max(l, r) + 1
        mmax = max(l + r + 1, lmax, rmax)
        return m, mmax

# Convert BST to Greater Tree
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        myroot = root
        self.postorder(root, 0)
        return myroot

    def postorder(self, root, mysum):
        if (root.right):
            mysum = self.postorder(root,right, mysum)
        root.val, mysum = root.val + mysum, mysum + root.val
        if (root.left):
            mysum = self.postorder(root,left, mysum)
        return mysum

# 01 Matrix
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m == 0:  return []
        n = len(matrix[0])
        res = [[-1] * n for _ in range(m)]
        mp = set([])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    for a, b in [(i+1, j),(i - 1, j), (i, j+1), (i, j -1)]:
                        if 0<=a<m and 0<=b<n and matrix[a][b] != 0:
                            res[a][b] = 1
                            mp |= {(a,b)}

        while(mp):
            i,j = mp.pop(0)
            step = res[i][j]
            for a, b in [(i+1, j),(i - 1, j), (i, j+1), (i, j -1)]:
                if (0<= a < m and 0 <= b < n) and (res[a][b] == -1 or res[a][b] > step + 1):
                    res[a][b] = step + 1
                    mp |= {(a,b)}

        return res

# Output Contest Matches
#
# During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're given n teams, you need to output their final contest matches in the form of a string.
#
# The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') to represent the contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.
#
# Example 1:
# Input: 2
# Output: (1,2)
# Explanation:
# Initially, we have the team 1 and the team 2, placed like: 1,2.
# Then we pair the team (1,2) together with '(', ')' and ',', which is the final answer.
# Example 2:
# Input: 4
# Output: ((1,4),(2,3))
# Explanation:
# In the first round, we pair the team 1 and 4, the team 2 and 3 together, as we need to make the strong team and weak team together.
# And we got (1,4),(2,3).
# In the second round, the winners of (1,4) and (2,3) need to play again to generate the final winner, so you need to add the paratheses outside them.
# And we got the final answer ((1,4),(2,3)).
# Example 3:
# Input: 8
# Output: (((1,8),(4,5)),((2,7),(3,6)))
# Explanation:
# First round: (1,8),(2,7),(3,6),(4,5)
# Second round: ((1,8),(4,5)),((2,7),(3,6))
# Third round: (((1,8),(4,5)),((2,7),(3,6)))
# Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
# Note:
# The n is in range [2, 212].
# We ensure that the input n can be converted into the form 2k, where k is a positive integer.
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        mylist = self.findcontest(n)
        k = n
        mystrings = [str(i) for i in mylist]
        while(k > 1):
            newstrings = []
            k /= 2
            for i in range(k):
                a = mystrings[i*2]
                b = mystrings[i*2+1]
                newstrings += ["(" + a + "," + b + ")"]
            mystrings = newstrings
        return mystrings[0]


    def findcontest(self, n):
        """
        :type n: int
        :rtype: str
        """
        mylist = [1]
        k = 1
        while(k < n):
            newlist = []
            k *= 2
            for i in mylist:
                newlist += [i]
                newlist += [k + 1 - i]
            mylist = newlist
        return mylist
