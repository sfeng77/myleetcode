"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        def linearSearch(array, target):
            return (target in array)

        def searchPart(matrix, xstart, xend, ystart, yend, target):
            print "Part search", xstart, xend, ystart, yend, target
            d = min(xend - xstart, yend - ystart)
            if d == 0:
                return False
            if d == 1:
                if xend - xstart == 1:
                    return linearSearch(matrix[xstart][ystart:yend],target)
                else:
                    return linearSearch([m[ystart] for m in matrix[xstart:xend]], target)
            mx, my = (xend + xstart) / 2, (yend+ystart)/2
            lx, ly = mx - d / 2, my - d / 2
            rx, ry = lx + d, ly + d

            while(matrix[mx][my] > target or matrix[mx+1][my+1] < target):
                print "x",lx, mx, rx
                print "y",ly, my, ry

                if matrix[mx][my] == target:
                    return True

                if matrix[mx][my] > target:
                    rx, ry = mx, my
                    mx, my = (lx + rx) / 2, (ly + ry) / 2
                else:
                    lx, ly = mx + 1 , my + 1
                    mx, my = (lx + rx) / 2, (ly + ry) / 2

            return searchPart(matrix, xstart, mx + 1, my + 1, yend, target) or searchPart(matrix, mx + 1, xend, ystart, my + 1, target)


        W, H = len(matrix), len(matrix[0])
        return searchPart (matrix, 0, W, 0, H, target)
