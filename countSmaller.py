# You are given an integer array nums and you have to return a new counts array
# The counts array has the property where counts[i] is the number of smaller
# elements to the right of nums[i].
#
# Example:
#
# Given nums = [5, 2, 6, 1]
#
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        vals = []
        n = len(nums)
        if n == 0:
            return []
        smaller = [0] * n
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_left(vals, nums[i])
            smaller[i] = j
            vals.insert(j, nums[i])
        return smaller
