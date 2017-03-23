"""

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

https://leetcode.com/problems/spiral-matrix/

"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dir = [(0,1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        i, j = 0, 0
        try:
            dim = [len(matrix), len(matrix[0])]
        except (TypeError, IndexError):
            return []
        visited = [[0] * dim[1] for _ in range(dim[0])]
        steps = 0
        guests = []
        while steps < dim[0] * dim[1]:
            visited[i][j] = 1
            guests.append(matrix[i][j])
            a = i + dir[d][0]
            b = j + dir[d][1]
            if a < 0 or a > dim[0]-1 or b < 0 or b > dim[1]-1 or visited[a][b]:
                d = (d+1) % 4
                a = i + dir[d][0]
                b = j + dir[d][1]
            i, j = a, b
            steps += 1
        return guests
