# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        n = len(nums)
        mysum = 0
        minLen = n
        for i in range(n):
            mysum += nums[i]
            if mysum >= s:
                while( start < n and mysum - nums[start] >= s):
                    mysum -= nums[start]
                    start += 1
                minLen = min(minLen, i - start + 1)
        if mysum < s:
            return 0
        return minLen
