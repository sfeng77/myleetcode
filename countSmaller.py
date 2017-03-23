# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
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


        l = []

        for val in nums:
            idx = self.binarySearch(l, val)
            if l[idx] != val:
                l = l[:idx] + [val] + l[idx:]

                d = {}
                res = [0] * len(nums)
                for i in range(len(nums), -1, -1):
                    val = nums[i]
                    res[i]= d.get(val, 0)
                    idx = self.binarySearch(l, val)

    def binarySearch(self, nums, val):
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = l + (r - l) / 2
            if nums[mid] < val:
                l = mid + 1
            elif nums[mid] > val:
                r = mid - 1
            else:
                return mid
        return l
