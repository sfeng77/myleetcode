# implements a template for bfs, dfs

class node(object):
    def __init__(self, id):
        self.id = id

    def neighbors(self):
        pass

    def dosomething(self):
        pass


class matrix2DNode(object):
    def __init__(self, id, dim):
        self.id = id
        self.dim = dim
        self.val = id

    def neighbors(self):
        i, j = self.id
        m, n = self.dim
        return [matrixNode((a,b),(m,n)) for (a,b) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0<=a<m if 0<=b <n]

    def dosomething(self):
        print self.val


class Solution(object):

    def BFS(self,root, target):
        visited = {root.id}
        from collections import deque
        q = deque([root])
        while(q):
            curr = q.popleft()
            curr.dosomething()
            if curr.val == target:
                return True
            for next in curr.neighbors():
                if next.id not in visited:
                    q.append(next)
                    visited.add(next.id)
        return False

    def DFS(self, root, target):
        visited = {root.id}
        s = [root]
        while(s):
            curr = s.pop()
            curr.dosomething()
            if curr.val == target:
                return True
            for next in curr.neighbors():
                if next.id not in visited:
                    s.append(next)
                    visited.add(next.id)
        return False
