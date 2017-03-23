"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000

"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        currLen = 0
        for i in nums:
            if i == 1:
                currLen += 1
            else:
                if currLen > maxLen:
                    maxLen = currLen
                currLen = 0
        if currLen > maxLen:
            maxLen = currLen
        return maxLen
