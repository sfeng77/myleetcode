# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        p = []
        for i in range( numRows):
            newrow = [1]
            if i > 0:
                for j in range(len(p[-1]) - 1):
                    newrow.append(p[-1][j] + p[-1][j+1])
                newrow.append(1)
            p.append(newrow)

        return p
        
