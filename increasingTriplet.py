#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
# Given [5, 4, 3, 2, 1],
# return false.
#
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:    return False
        smallest = nums[0]
        secondSmallest = max(nums)
        for i in nums:
            #print smallest, secondSmallest, i
            if i > secondSmallest:  return True
            if i < smallest:
                smallest = i
            elif i > smallest and i < secondSmallest:
                secondSmallest = i
        return False
