#Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        lines = {}


        def findLine(a, b):
            if a.x != b.x:
                k = (a.y - b.y) / (a.x - b.x)
                y0 = a.y - k * a.x
                return (True, k , y0)
            else:
                x0 = a.x
                return (False, x0, 0)


        n = len(points)
        duplicates = [1] * n
        for i in range(n - 1):
            pointI = points[i]
            for j in range(i+1 ,n):
                pointJ = points[j]
                if pointI == pointJ:
                    duplicates[i] += 1
                    duplicates[j] = 0
                    continue

                myline = findLine (pointI, pointJ)
                if myline in lines:
                    lines[myline] += [j]
                else:
                    lines[myline] = [i,j]

        maxLines = min(2, n)
        for l in lines:
            myCount = [duplicates[i] for i in lines[l]]
            maxlines = max(maxLines, myCount)
        return maxLines
