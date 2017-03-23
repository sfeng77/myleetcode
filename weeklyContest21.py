#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Solution():
# Definition for a binary tree node.

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = self.inorderTraversal(root)
        n = len(res)
        diff = 0
        if n >= 2:
            diff = abs(res[1] - res[0])
        for i in range(n - 1):
            diff = min(diff, abs(res[i+1] - res[i]))

        return diff



    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        dp = [0] * (n + 1)
        mySum = 0
        for i in range(n):
            mySum += nums[i]
            dp[i+1] = mySum

        for i in range(n-1):
            for j in range(i+2, n + 1):
                if (k == 0):
                    if dp[j] == dp[i]:
                        return True
                elif (dp[j] - dp[i] ) % k == 0:
                    return True

        return False


    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        board = [list(l) for l in board]
        m = len(board)
        if m == 0:  return board
        n = len(board[0])
        if n == 0:  return board
        res = [l[:] for l in board]
        print board
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'M':
                    continue
                neighborSum = 0
                for a in [i-1, i, i +1]:
                    for b in [j-1, j, j + 1]:
                        if a >= 0 and a < m and b >= 0 and b < n and board[a][b] == 'M':
                            neighborSum += 1
                board[i][j] = neighborSum

        x, y = click


        if board[x][y] == 'M':
            res[x][y] = 'X'
            return res

        if board[x][y] != 0:
            res[x][y] = str(board[x][y])
            return res

        front = [(x,y)]
        res[x][y] = 'B'
        while(front):
            i, j = front.pop()
            for a in [i-1, i, i +1]:
                for b in [j-1, j, j + 1]:
                    if a == i and b == j:   continue
                    if a >= 0 and a < m and b >= 0 and b < n:
                        #print board[a][b], res[a][b]
                        if board[a][b] == 0 and res[a][b] == 'E':
                            front += [(a,b)]
                            res[a][b] = 'B'
                        elif board[a][b] != 'M' and board[a][b] > 0:
                            res[a][b] = str(board[a][b])
        return res

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        sol = {}
        m = len(s)
        for w in d:
            if self.isPart(s,w):
                diff = m - len(w)
                sol[diff] =  sol.get(diff, []) + [w]
        k = min(sol.keys())
        return sorted(sol[k])[0]

    def isPart(self, s, t):
        m, n = len(s), len(t)
        if m < n:
            return False
        i, j= 0, 0
        while(j < n):
            while(i < m - n + j + 1):
                #print i, j
                if s[i] == t[j]:
                    j += 1
                    if j == n:
                        return True
                i += 1
            return False
