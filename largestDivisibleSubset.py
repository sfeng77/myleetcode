# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or
# Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        if n == 0:
            return []
        pre = range(n)
        count = [0] * n

        for i in range(0, n):
            ni = nums[i]
            count[i], pre[i] = max([(count[j] + 1 if ni % nums[j] == 0 else 0, j)
                                    for j in range(i + 1)])

        _, maxid = max(zip(count, range(n)))
        res = [nums[maxid]]
        while(pre[maxid] != maxid):
            maxid = pre[maxid]
            res.append(nums[maxid])

        return res
