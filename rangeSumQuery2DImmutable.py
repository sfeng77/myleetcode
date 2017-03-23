class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if matrix!=[]:
            m=len(matrix)
            n=len(matrix[0])
            sums=[[0]*n for _ in xrange(m)]
            sums[0][0]=matrix[0][0]
        
            for i in xrange(1,m):
                sums[i][0]=sums[i-1][0]+matrix[i][0]
            for j in xrange(1,n):
                sums[0][j]=sums[0][j-1]+matrix[0][j]

            for i in xrange(1,m):
                for j in xrange(1,n):
                    sums[i][j]=sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + matrix[i][j]

            self.sums=[[0]+row for row in sums]
            self.sums=[[0]*(n+1)]+self.sums

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2+1][col2+1]-self.sums[row2+1][col1]-self.sums[row1][col2+1]+self.sums[row1][col1]
