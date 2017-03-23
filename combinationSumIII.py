"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def combinationSum(k, n , m):
            if (k + m) > 10 or k * (2 * m - k +1) / 2 > n or k * (2 * 9 -k + 1) / 2 < n:
                return []
            if k == 1:   return [[n]]
            return [[i]+l for i in range(m, 9) for l in combinationSum(k - 1, n - i, i + 1)]

        return combinationSum(k,n,1)
