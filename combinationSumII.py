"""
 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def combinationSumII(candidates, target):
            if target < 0:  return []
            r = set([])
            for i in range(len(candidates)):
                c = candidates[i]
                if c > target:  break
                if c == target:
                    r.add((c,))
                else:
                    r.update([(c,)+l
                        for l in combinationSumII(candidates[i+1:], target - c)])
            return r

        return [list(l) for l in combinationSumII(sorted(candidates), target)]
