"""

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

"""

#Accepted but very slow
#better using heap: https://discuss.leetcode.com/topic/60624/python-solution-with-heap



class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        try:
            dim = [len(heightMap), len(heightMap[0])]
        except IndexError:
            return 0
        if dim[0] < 3 or dim[1] < 3:
            return 0

        maxRim = [[[0] * dim[1] for _ in range(dim[0])] for _ in range(4)]

        for i in range(1, dim[0] - 1):
            for j in range(1, dim[1] - 1):
                maxRim[0][i][j] = max(maxRim[0][i - 1][j], heightMap[i - 1][j])

        for i in range(dim[0] - 2, 0, -1):
            for j in range(1, dim[1] - 1):
                maxRim[1][i][j] = max(maxRim[1][i + 1][j], heightMap[i + 1][j])

        for j in range(1, dim[1] - 1):
            for i in range(1, dim[0] - 1):
                maxRim[2][i][j] = max(maxRim[2][i][j - 1], heightMap[i][j - 1])

        for j in range(dim[1] - 2, 0, -1):
            for i in range(1, dim[0] - 1):
                maxRim[3][i][j] = max(maxRim[3][i][j + 1], heightMap[i][j + 1])

        waterLevel = [[min([maxRim[_][i][j] for _ in range(4)]) for j in range(dim[1])] for i in range(dim[0])]
        leak = 1

        def checkLeak(i,j):
            if waterLevel[i][j] <= heightMap[i][j]:
                return False
            neighborMax = min([max(waterLevel[a][b], heightMap[a][b]) for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]])
            if waterLevel[i][j] > neighborMax :
                waterLevel[i][j] = neighborMax
                return True
            return False

        leakMap = set([(i,j) for i in range(1, dim[0]-1) for j in range(1, dim[1] - 1)])
        while (leakMap):
            i,j = leakMap.pop()
            if checkLeak(i, j):
                for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    leakMap.add((a,b))

        #waterMap = [min([maxRim[_][i][j] for _ in range(4)]) - heightMap[i][j] for i in range(dim[0]) for j in range(dim[1])]
        trappedWater = [max(0, waterLevel[i][j] - heightMap[i][j]) for i in range(dim[0]) for j in range(dim[1])]

        return sum(trappedWater)
