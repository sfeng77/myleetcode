# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
#
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
#
# Answer: 3
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:    return 0
        grid = [list(s) for s in grid]
        m = len(grid)
        n = len(grid[0])
        neighbors = []
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    neighbors += [(i,j)]
                    while(neighbors):
                        p, q = neighbors.pop()
                        grid[p][q] = '0'
                        neighbors += [(k,l) for (k,l) in [(p-1, q), (p+1, q), (p, q-1), (p , q+1)] if 0<=k < m if 0<=l <n if grid[k][l] == '1']
                    count += 1
        return count
