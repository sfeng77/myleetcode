 # Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#https://discuss.leetcode.com/topic/2031/challenge-me-thx/17

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for v in nums:
            ones = (ones ^ v) & ~twos
            twos = (twos ^ v) & ~ones
        return ones
