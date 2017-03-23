#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Solution():
# Definition for a binary tree node.

    def order(a,b):
        if a <= b:
            return (a,b)
        else:
            return (b,a)

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:   return 0
        n = len(nums)
        if n < 2:
            return 0
        d = set([])
        res = set([])
        for i in range(n):
            v = nums[i]
            if v + k in d:
                res.add(order(v,v+k))
            if v - k in d:
                res.add(order(v,v-k))
            d.add(v)
        return len(res)



    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        m = len(picture)
        if m < 1:   return 0
        n = len(picture[0])
        if n < 1:   return 0

        d1 = {}
        d2 = {}

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    d1[i] = d1.get(i, []) + [j]
                    d2[j] = d2.get(j, []) + [i]
        sum = 0
        for i in d1:
            if len(d1[i]) == 1 and len(d2[d1[i][0]]) == 1:
                sum += 1
        return sum


    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        m = len(picture)
        if m < 1:   return 0
        n = len(picture[0])
        if n < 1:   return 0

        d1 = {}
        d2 = {}

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    d1[i] = d1.get(i, []) + [j]
                    d2[j] = d2.get(j, []) + [i]
        sum = 0
        for i in d1:
            if len(d1[i]) != N:
                continue
            print d1[i]
            for j in d1[i]:
                if len(d2[j])!= N:
                    continue
                flag = True
                for r in d2[j]:
                    print d1[r]
                    if d1[r] != d1[i]:
                        flag = False
                        break
                if flag:
                    sum += 1
                    print i,j
        return sum


    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        import heapq

        d = {}
        nr = len(ring)
        nk = len(key)
        MAX = nr * nk + 1
        for i in range(nr):
            c = ring[i]
            d[c] = d.get(c, []) + [i]

        def minStep(pos, c):
            loc = d[c]
            sol = []
            for i in loc:
                heapq.heappush(sol, (min((i + nr - pos) % nr, (- i + nr + pos) % nr), i))
            return sol

        myMap = [[MAX] * nr for _ in range(nk)]
        pos = [0]
        totalSteps = 0
        for s,p in minStep(0, key[0]):
            myMap[0][p] = s + 1
        for i in range(1, nk):
            mykey = key[i]
            #print mykey
            for pos in d[key[i-1]]:
                for s, p in minStep(pos, mykey):
                    #print s, p
                    myMap[i][p] = min(myMap[i][p], s + myMap[i-1][pos] + 1)
            #print myMap[i][p]
        #print myMap
        return min(myMap[nk-1])
