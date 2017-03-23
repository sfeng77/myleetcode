#  Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        step = 0
        stepCount = 0
        maxStep = 0
        while(True):
            print step
            maxStep = step + 1
            nextStep = step + 1
            for i in range(step + 1, step + nums[step] + 1):
                if i == n - 1:
                    return stepCount + 1
                s = i + nums[i]
                print i, nums[i]
                if s > maxStep:
                    maxStep = s
                    nextStep = i
            step = nextStep
            stepCount += 1
