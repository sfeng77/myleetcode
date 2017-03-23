# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
#
# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
#
# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
#
# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
# -2 (K) 	-3 	3
# -5 	-10 	1
# 10 	30 	-5 (P)
#
# Notes:
#
#     The knight's health has no upper bound.
#     Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        mymap = [[1] * n for _ in range(m)]
        mymap[m-1][n-1] = max(1 -dungeon[m-1][n-1] , 1)

        for i in range(m - 2, -1, -1):
            mymap[i][n - 1] = max(mymap[i+1][n-1] - dungeon[i][n-1] , 1)

        for j in range(n -2, -1, -1):
            mymap[m-1][j] = max(mymap[m-1][j+1] - dungeon[m-1][j], 1)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                h = min(mymap[i][j+1], mymap[i+1][j])
                mymap[i][j] = max(h - dungeon[i][j], 1)

        #print mymap
        return mymap[0][0]
