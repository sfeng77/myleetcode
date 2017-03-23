"""
 Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

"""

import math

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        d = {}

        def combinationSum(nums, target):
            try:
                c = nums[0]
            except IndexError:
                return []
            if len(nums) == 1:
                if target % c == 0:
                    return [[target / c]]
                else:
                    return []
            t = (tuple(nums), target)
            if t in d:
                return d[t]

            r = []
            for i in range(0, target / c):
                r += [[i] + l for l in combinationSum(nums[1:], target - c * i)]
            if target % c == 0:
                r += [[target / c ]]
            d[t] = r
            return r

        rl = combinationSum(sorted(nums), target)
        print rl
        c = 0
        for r in rl:
            n = math.factorial(sum(r))
            for i in r:
                n /= math.factorial(i)
            c += n
        return c
