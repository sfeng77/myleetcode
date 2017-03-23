"""

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        doublets = {}
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                sum = nums[i] + nums[j]
                doublets[sum] = [(i,j)] + doublets.get(sum, [])

        res = set([])
        for sum in doublets:
            for i, j in doublets[sum]:
                for k, l in doublets.get(target - sum,[]):
                    if len(set([i,j,k,l])) == 4:
                        res.add(tuple(sorted([nums[a] for a in [i,j,k,l]])))
        return [list(s) for s in res]
