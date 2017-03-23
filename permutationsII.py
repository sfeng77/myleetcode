# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)

        if n < 2:
            return [nums]
        nums.sort()
        permutations = [[nums[0]]]
        nextPermutations = []
        for val in nums[1:]:
            for p in permutations:
                for i in range(0,len(p)+1):
                    if i==len(p) or p[i] != val:
                        nextPermutations += [p[:i] + [val] + p[i:]]
            permutations = nextPermutations[:]
            nextPermutations = []

        return permutations
