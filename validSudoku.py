class Solution(object):
    def __init__(self):
        self.rowMask=[(0b111111111) << (i*9) for i in range(9)]
        self.colMask=[(0b1000000001000000001000000001000000001000000001000000001000000001000000001) << i for i in range(9)]
        self.boxMask=[0]*9
        for i in range(3):
            for j in range(3):
                self.boxMask[i*3+j] =  0b111000000111000000111 << (i*27+j*3)
        self.d={str(i+1):i for i in range(9)}
        self.d['.']=-1
        

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        mask=[[0]*9 for _ in xrange(9)]
        for i in xrange(9):
            for j in xrange(9):
                val = self.d[board[i][j]]
                if val > -1:
                    if (mask[i][j]>>val) & 1:
                        return False
                    for n in xrange(j,9):
                        mask[i][n] |= (1 << val)
                    for m in xrange(i,9):
                        mask[m][j] |= (1 << val)
                    for m in xrange(3):
                        for n in xrange(3):
                            mask[i/3*3+m][j/3*3+n] |= (1<< val)
        return True


    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        mask=[0] * 9
        for i in xrange(9):
            for j in xrange(9):
                val = self.d[board[i][j]]
                if val > -1:
                    if (mask[val] >> (i*9+j)) & 1:
                        return False
                    mask[val] |= self.rowMask[i]
                    mask[val] |= self.colMask[j]
                    mask[val] |= self.boxMask[i/3*3+j/3]
        return True
