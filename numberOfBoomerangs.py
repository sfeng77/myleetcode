# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)
        count = 0
        distance = [[0] * n for _ in range(n)]
        for i in range(n):
            mydistance = {}
            for j in range(n):
                if j > i:
                    d = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) **2
                    distance[i][j] = d
                else:
                    d = distance[j][i]
                mydistance[d] = mydistance.get(d, 0) + 1

            for k in mydistance.keys():
                p = mydistance[k]
                count += p * (p - 1)
    #        print mydistance, count
        return count
