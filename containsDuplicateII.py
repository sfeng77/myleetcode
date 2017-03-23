# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        seen = {}
        for i in range(n):
            a = nums[i]
            if a not in seen:
                seen[a] = i
            else:
                if i - seen[a] <= k:
                    return True
                else:
                    seen[a] = i
        return False
