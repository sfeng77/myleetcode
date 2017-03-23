#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hp = []
        for c in nums:
            heapq.heappush(hp, c)
            if len(hp) > k:
                heapq.heappop(hp)
        return hp[0]
