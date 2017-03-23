
class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str

        """
        m = len(maze)
        n = len(maze[0])
        #print m, n

        myMap = [['' for _ in  range(n)] for _ in range(m)]
        #print myMap
        dirs = { 'd':(1,0), 'l':(0, -1), 'r':(0, 1), 'u': (-1, 0)}
        newMove = 1
        myMap[ball[0]][ball[1]] = 'b'
        #print myMap

        def findWall(i,j,d):
            di, dj = dirs[d]
            ni, nj = i + di, j + dj
            while(myMaze(ni,nj)==0 and [i,j] != hole):
                i, j = ni, nj
                ni, nj = i + di, j + dj
                #print i,j,ni,nj
            return i, j

        def myMaze(i,j):
            #print i,j, m,n
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            else:
                return maze[i][j]

        def compareString(a,b):
            if a == '':
                return b
            if len(a) == len(b):
                if a < b:
                    return a
                else:
                    return b
            elif len(a) < len(b):
                return a
            else:
                return b


        def findPathLength(s):
            pos = ball
            pathLen = 0
            if s == 'b':
                return 0
            for d in s:
                i, j = pos
                ni,nj = findWall(i,j,d)
                pathLen += abs(ni -i) + abs(nj-j)
            return pathLen

        def comparePath(a,b):
            la = findPathLength(a)
            lb = findPathLength(b)
            if la< lb:
                return a
            else:
                return b

        sol = ''
        while(newMove):
            newMove = 0
            for i in range(m):
                for j in range(n):
                    if myMap[i][j]:
                        mm = myMap[i][j]
                        #print mm
                        for d in ['d', 'l', 'r', 'u']:
                            wi, wj = findWall(i,j,d)
                            #print wi, wj
                            if [wi,wj] == hole:
                                #print "Reach hole"
                                s = comparePath(sol, mm + d)
                                print s, sol
                                if sol != s:
                                    sol = s
                                    newMove += 1
                                continue
                            s = comparePath(myMap[wi][wj], mm + d)
                            if s != myMap[wi][wj]:
                                myMap[wi][wj] = s
                                newMove += 1

        #print myMap
        #print sol
        return sol[1:]
