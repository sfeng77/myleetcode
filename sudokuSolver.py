class Solution(object):
    def __init__(self):
        self.rowMask=[(0b111111111) << (i*9) for i in range(9)]
        self.colMask=[(0b1000000001000000001000000001000000001000000001000000001000000001000000001) << i for i in range(9)]
        self.boxMask=[0]*9
        self.fullmask=0b111111111111111111111111111111111111111111111111111111111111111111111111111111111
        for i in range(3):
            for j in range(3):
                self.boxMask[i*3+j] =  0b111000000111000000111 << (i*27+j*3)
        self.d={str(i+1):i for i in range(9)}
        self.d['.']=-1

    def maskElement(self, mask, i,j,val):
        mask[val] |= self.rowMask[i]
        mask[val] |= self.colMask[j]
        mask[val] |= self.boxMask[i/3*3+j/3]
        m = 0b1 << (i*9+j)
        mask[:]=map(lambda x:x|m, mask)
                
    def findMask(self,board):
        mask=[0] * 9
        for i in xrange(9):
            for j in xrange(9):
                try:
                    val = self.d[board[i][j]]
                except KeyError:
                    print i,j,board[i][j]
                if val > -1:
                    self.maskElement(mask,i,j,val)
        return mask
   
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board_list=[list(item) for item in board]
        mask=self.findMask(board_list)
        bB=self.bitBoard(board_list)
        result=self.solveWithMask(board_list,mask,bB)
        board[:] = map(''.join,self.bbToBoard(result))
#        if result == -1:
#            print "not solvable!"
#        else:
#            return map(''.join,self.bbToBoard(result))

    def zeroPossibility(self,mask):
        #find cells where no numbers are allowed
        return reduce(lambda x,y:x & y, mask)

    def onePossibility(self,mask):
        #find cells where only 1 number is allowed
        p1=[0]*9
        for i in xrange(9):
            p1[i] = self.fullmask ^ mask[i]
            for j in xrange(9):
                if j!=i:
                    p1[i] &= mask[j]
        return p1

    def sudokuFinished(self, bB):
        if ((reduce(lambda x,y: x|y, bB) == 0b111111111111111111111111111111111111111111111111111111111111111111111111111111111)
            and (reduce(lambda x,y:x&y,bB)== 0)):
            return True
        else:
            return False

    def bitBoard(self,board):
        bB=[0]*9
        for i in xrange(9):
            for j in xrange(9):
                try:
                    val = self.d[board[i][j]]
                except KeyError:
                    print i,j,board[i][j]
                if val > -1:
                    bB[val] |= 0b1 << (i*9+j)
        return bB

    def bbToBoard(self, bB):
        board=[['.']*9 for _ in xrange(9)]
        for pos in xrange(81):
            for val in xrange(9):
                if (bB[val]>>pos)&1:
                    board[pos/9][pos%9]=str(val+1)
        return board
    
    
    def fillSolePossibility2(self,board,mask,bB):
#        if mask is None:
#            mask=self.findMask(board)
#        if bB is None:
#            bB=self.bitBoard(board)

        p0 = self.zeroPossibility(mask)
        if (p0 ^ reduce(lambda x,y:x|y, bB)):
            return -1, mask, bB
        
        p1 = self.onePossibility(mask)
        count = 0
        for i in xrange(9):
            update=0
            pos=0
            bB[i] |= p1[i]
            while(p1[i]):
                if (p1[i]&1):
                    if (update >> pos) & 1:
                        #conflicting updates
                        return -1, mask, bB
                    x=pos/9
                    y=pos%9
                    update |= (self.rowMask[x] | self.colMask[y] | self.boxMask[x/3*3+y/3])
                    count += 1
                pos += 1
                p1[i] = p1[i] >> 1
            mask[i] |= update
        if count >0:
             return self.fillSolePossibility2(board,mask,bB)
        else:
            return count, mask, bB
        
        
    def solveWithMask(self, board, mask, bB, rc=0):
        if (rc>50):
            print "recursion limit reached!"
            print "mask=",mask
            print "bb=",bB
            return -1

        ret,mask,bB=self.fillSolePossibility2(board, mask, bB)
        if ret==-1:
            return -1
        if self.sudokuFinished(bB):
            return bB
        vals=[0]*9
        pos=-1
        while(sum(vals)==0):
            pos +=1
            vals= map(lambda x: 1 ^((x>>pos) & 1), mask)
        val=0
        for val in xrange(9):
            if (vals[val]):
                newMask=mask[:]
                newBB=bB[:]
                self.maskElement(newMask,pos/9,pos%9,val)
                newBB[val] |= 0b1<<pos
                result=self.solveWithMask(board,newMask,newBB,rc+1)
                if result!=-1:
                    return result
        return -1
        

class obsolete():
    def fillSolePossibility(self,board,mask=None):
        if not mask:
            mask=self.findMask(board)
        moves=self.possibleMoves(mask)
        countMovesPerCell = [[len(moves[i]),i] for i in range(81)]
        countMovesPerCell.sort()
        i=0
        while(countMovesPerCell[i][0]==0):
            pos=countMovesPerCell[i][1]
            if board[pos/9][pos%9]=='.':
                print "not valid!"
                return -1
            i+=1
        count = 0
        while(countMovesPerCell[i][0]==1):
            pos=countMovesPerCell[i][1]
            val=moves[pos][0]
            x,y=pos/9,pos%9
            board[x][y]=str(val+1)
            mask[val] |= self.rowMask[x]
            mask[val] |= self.colMask[y]
            mask[val] |= self.boxMask[x/3*3+y/3]
            for k in range(9):
                mask[k] |= 0b1 << (x*9+y)
            i+=1
            count += 1
        if count >0:
            ret=self.fillSolePossibility(board,mask)
            if ret==-1:
                return -1
        else:
            return count
        
    def possibleMoves(self,mask):
        return [[val for val in range(9) if (mask[val] >> pos &1 == 0)] for pos in xrange(81)]
