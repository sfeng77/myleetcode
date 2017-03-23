"""
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:    return []
        currSum = 0
        minSum = 0
        maxSum = 0
        maxId = 0
        minId = 0


        for i in range(0,len(nums)):
            currSum += nums[i]
            if maxSum <= currSum:
                maxSum = currSum
                maxId = i
            if minSum > currSum:
                minSum = currSum
                minId = i
            print "max:", maxSum, maxId
            print "min:", minSum, minId

        return nums[minId:maxId+1]
