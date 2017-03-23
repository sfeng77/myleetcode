"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

#DFS + up-down DP

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dmap = {}
        try:
            m, n = len(matrix), len(matrix[0])
        except IndexError:
            return 0

        def discoverMap(i,j,matrix):
            if (i,j) not in dmap:
                paths = [discoverMap(k, l, matrix ) for k, l in [(i, j+1), (i, j-1), (i-1, j),(i+1, j)] if 0<=k<m if 0<=l<n if matrix[k][l] > matrix[i][j] ]
                if paths:
                    dmap[(i,j)] = 1 + max(paths)
                else:
                    dmap[(i,j)] = 1
            return dmap[(i,j)]

        return max([discoverMap(i,j,matrix) for i in range(m) for j in range(n)])
