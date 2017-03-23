class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        m = len(findNums)
        n = len(nums)
        if not nums:
            return []
        res = [-1] * m
        loc = {}
        j = 0
        loc[nums[0]] = 0
        for i in range(m):
            a = findNums[i]
            if a not in loc:
                while(nums[j] != a):
                    j += 1
                    loc[nums[j]] = j
                    #print loc
            for k in range(loc[a] + 1, n):
                if nums[k] > a:
                    res[i] = nums[k]
                    break
        return res


    def nextGreaterElementsII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if not nums:
            return []
        res = [-1] * n
        maxRight=[0] * n
        maxRight[n-1] = nums[n-1]
        for i in range(n-2, -1 ,-1):
            maxRight[i] = max(maxRight[i+1], nums[i])
        for i in range(n):
            j = (i + 1) % n
            a = nums[i]
            if maxRight[i] <= a:
                j = 0
            while(j != i):
                if nums[j] > a:
                    res[i] = nums[j]
                    break
                j = (j+1) % n
        return res


    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        a = sorted(zip(nums,range(n)),key =  lambda x:x[0], reverse = True)
        res = [''] * n
        d = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(n):
            if i < 3:
                res[a[i][1]] = d[i]
            else:
                res[a[i][1]] = str(i + 1)
        return res


    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        res = []

        for sumIJ in range(m + n - 1 ):
            d = sumIJ % 2
            if d == 0:
                if sumIJ < m:
                    j = 0
                    i = sumIJ
                else:
                    i = m - 1
                    j = sumIJ - i
                while((j < n) and (i >= 0)):
                    res.append(matrix[i][j])
                    j += 1
                    i -= 1
            else:
                if sumIJ < n:
                    i = 0
                    j = sumIJ
                else:
                    j = n -1
                    i = sumIJ - j
                while((j >= 0) and (i < m)):
                    res.append(matrix[i][j])
                    j -= 1
                    i += 1

        return res
