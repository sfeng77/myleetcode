class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for v in nums:
            s = s ^ v
        return s
