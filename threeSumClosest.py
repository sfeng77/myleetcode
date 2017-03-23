# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:   return []
        nums.sort()
        res = sum(nums[:3])
        for i in range(n - 2):
            if (i > 0) and nums[i] == nums[i - 1]: continue
            j = i + 1
            k = n -  1
            while(j < k):
                mysum = nums[i] + nums[j] + nums[k]
                if abs(res - target) > abs(mysum - target):
                    #print i,j,k,nums[i] + nums[j] + nums[k]
                    res = mysum
                if mysum == target:
                    return target
                elif mysum > target:
                    k -= 1
                else:
                    j += 1
        return res
