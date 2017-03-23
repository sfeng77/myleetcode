"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 <= k <= n <= 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

"""

import math

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def find(n, k, m):
            from math import log10
            print n
            l = int(log10(n - 1))
            base  = int('1'*(l+1))
            p, q = n / 10 ** l, n % (10 ** l)
            s = [base] * (p) + [q+ base / 10 + 1] + [base / 10] * (9 - p)
            t = [10**l] * (p) + [q + 1] + [10 ** (l-1)] * (9 - p)
            first = m
            print s, n, k
            while(k > s[first]):
                k -= s[first]
                first += 1
            print first, k
            if k > 1:
                return str(first) + str(find(t[first] - 1, k - 1, 0))
            else:
                return str(first)

        return int(find(n, k , 1))

    def generateKthNumber(self, n, k):
        return sorted(range(1,n+1), key = lambda x: str(x))[k-1]
