# Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.
#
# Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.
#
# Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.
#
# Examples:
#
# Input: "WRRBBW", "RB"
# Output: -1
# Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
#
# Input: "WWRRBBWW", "WRBRW"
# Output: 2
# Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
#
# Input:"G", "GGGGG"
# Output: 2
# Explanation: G -> G[G] -> GG[G] -> empty
#
# Input: "RBYYBBRRB", "YRBGB"
# Output: 3
# Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        from collections import Counter
        h = Counter(hand)
        n = len(board)
        l = []
        i = 0
        need = Counter()
        while(i < n):
            c = board[i]
            i += 1
            count = 1
            while(i<n and c == board[i]):
                i += 1
                count += 1
            l += [(c, count)]
        #print l

        for c, count in l:
            if need[c] == 0:
                need[c] = 3 - count
            elif need[c] < count:
                need[c] = 0
            else:
                need[c] -= count
            #print need

        for c in need:
            if need[c] > h[c]:
                return -1
        return sum(need.values())
