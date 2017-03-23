class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rowSets = [ set("QWERTYUIOP"), set("ASDFGHJKL"), set("ZXCVBNM")]
        res = []
        for w in words:
            s = set(w.upper())
            for r in rowSets:
                if s <= r:
                    res += [w]
        return res


    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sums = {}
        if not root:
            return []

        def subSum(root, sums):
            if not root:
                return 0
            mySum = subSum(root.left,sums) + subSum(root.right,sums) + root.val
            sums[mySum] = sums.get(mySum, 0) + 1
            return mySum

        subSum(root, sums)
        maxVal = max(sums.values())
        res = []
        for k in sums.keys():
            if sums[k] == maxVal:
                res += [k]
        return res


    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import heapq
        projects = sorted(zip(Profits, Capital), key=lambda x:x[1])

        hp = []
        n = len(projects)
        done = 0
        for p in projects:
            #print p, W, hp
            if p[1] <= W:
                heapq.heappush(hp, -p[0])
                continue
            if not hp:
                break
            W -= heapq.heappop(hp)
            done +=1
            if p[1] <= W:
                heapq.heappush(hp, -p[0])
            if done == k:
                break
        #print done, W, hp
        for i in range(done, k):
            if not hp:
                break
            W -= heapq.heappop(hp)
        return W
