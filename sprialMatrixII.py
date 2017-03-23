# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
# You should return the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dir = [(0,1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        i, j = 0, 0
        matrix = [[0] * n for _ in range(n)]
        visited = [[0] * n for _ in range(n)]
        steps = 0
        while steps < n * n:
            visited[i][j] = 1
            matrix[i][j] = steps + 1
            a = i + dir[d][0]
            b = j + dir[d][1]
            if a < 0 or a > n-1 or b < 0 or b > n-1 or visited[a][b]:
                d = (d+1) % 4
                a = i + dir[d][0]
                b = j + dir[d][1]
            i, j = a, b
            steps += 1
        return matrix
