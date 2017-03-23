class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid==[]:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        paths=[[0]*(n+1) for _ in xrange(m+1)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            paths[1][1]=1
            j=0
            while(j<n and obstacleGrid[0][j]==0):
                paths[1][j+1]=1
                j+=1
            for i in range(1,m):
                for j in range(n):
                    if obstacleGrid[i][j]!=1:
                        paths[i+1][j+1]=paths[i][j+1]+paths[i+1][j]
            return paths[m][n]
        
