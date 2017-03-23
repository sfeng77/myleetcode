# Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
#
# Note:
# If n is the length of array, assume the following constraints are satisfied:
#
#     1 <= n <= 1000
#     1 <= m <= min(50, n)
#
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l = max(nums)
        r = sum(nums)
        n = len(nums)

        def canSplit(nums, m, mysum):
            s = 0
            for i in range(n):
                #print s, nums[i], m
                if s + nums[i] <= mysum:
                    s += nums[i]
                else:
                    s = nums[i]
                    m -= 1
            if m < 1:
                return False
            else:
                return True

        while(l < r):
            mid = (l + r) / 2
            #print l, r, mid
            if canSplit(nums, m, mid):
                r = mid
            else:
                l = mid + 1
        return l
