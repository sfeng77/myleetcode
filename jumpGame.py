"""
 Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

#Accepted

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = nums[0]
        i = 0
        while(i < f and i < len(nums) - 1):
            i += 1
            f = max(f, nums[i] + i)

        if i < len(nums) -1 :
            return False
        else:
            return True
