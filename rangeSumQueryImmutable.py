class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n=len(nums)
        self.sums=[0]*n
        sum=0
        for i in xrange(n):
            sum = sum+nums[i]
            self.sums[i]=sum
        self.sums=[0]+self.sums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1]-self.sums[i]
