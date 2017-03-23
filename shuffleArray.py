# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        self.idx = range(self.n)

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        self.idx[i], self.idx[j] = self.idx[j], self.idx[i]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        for i in range(self.n):
            self.swap(i, self.idx[i])
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from random import randint
        for i in range(self.n - 1, 0, -1):
            j = randint(0, i - 1)
            self.swap(i,j)
        return self.nums
