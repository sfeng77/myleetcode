# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)

        if n < 2:
            return [nums]

        permutations = [[nums[0]]]
        nextPermutations = []
        for val in nums[1:]:
            for p in permutations:
                for i in range(0,len(p)+1):
                    nextPermutations += [p[:i] + [val] + p[i:]]
            permutations = nextPermutations[:]
            nextPermutations = []
        return permutations
