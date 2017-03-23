"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""

##ACCEPTED

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.dim = [len(board), len(board[0])]
        self.board = board
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if (board[i][j] == word[0]) and self.searchNeighbors((i,j), word[1:], [(i,j)]):
                    return True
        return False

    def searchNeighbors(self, loc, word, used ):
        if word == '':
            return True
        neighborList = []
        i, j = loc

        # find all valid neighbors
        if i > 0:   neighborList.append((i-1,j))
        if j > 0:   neighborList.append((i,j-1))
        if i < self.dim[0]-1:   neighborList.append((i+1,j))
        if j < self.dim[1]-1:   neighborList.append((i,j+1))

        for loc in neighborList:
            if loc not in used and self.board[loc[0]][loc[1]] == word[0] and self.searchNeighbors(loc, word[1:], used+[loc]):
                #letter not used         letter match the next letter in word       the neighbors match the residue of the word
                return True
        return False
