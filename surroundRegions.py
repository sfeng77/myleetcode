"""
 Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

"""

# This guy is a fucking genius
# https://discuss.leetcode.com/topic/18706/9-lines-python-148-ms

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        neighbors = []
        try:
            m, n = [len(board) , len(board[0])]
        except KeyError:
            return

# O_o
        qi = [ij for k in range(max(m,n)) for ij in ((0,k), (m - 1, k), (k, 0), (k, n - 1))]

        while (qi):
            i,j =qi.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = "Q"
                qi += (i, j - 1), (i - 1, j), (i + 1, j), (i, j + 1)

#o_O
        board[:] = [["XO"[c == "Q"] for c in row] for row in board]
