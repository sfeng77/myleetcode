# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
class Solution(object):
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        elements = dict(zip(nums, range(n)))
        res = []
        for i in range(n-2):
            for j in range(i+1, n - 1):
                s = -(nums[i]+nums[j])
                if s in elements:
                    if elements[s] > j:
                        res += [[nums[i],nums[j], s]]
                    else:
                        break
        return [[i,j,k] for i,j,k in set((a,b,c) for a,b,c in res)]


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:   return []
        nums.sort()
        res = []
        for i in range(n - 2):
            if (i > 0) and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = n -  1
            while(j < k):
                mysum = nums[i] + nums[j] + nums[k]
                #print i,j,k,nums[i], nums[j], nums[k]
                if mysum == 0:
                    res += [[nums[i], nums[j], nums[k]]]
                    while(j < k and nums[j+1] == nums[j]):  j += 1
                    while(j < k and nums[k-1] == nums[k]):  k -= 1
                    j += 1
                    k -= 1
                elif mysum > 0:
                    k -= 1
                else:
                    j += 1
        return res
