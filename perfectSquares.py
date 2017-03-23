"""
 Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

#ACCEPTED

class Solution(object):


    def __init__(self):
        self.d = {0:0}

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        if n not in self.d:
            m = n
            for i in range(int(sqrt(n)), 0, -1):
                if i * i * m < n:
                    break
                k = self.numSquares(n - i * i)
                m = min(m, k + 1)
            self.d[n] = m
        return self.d[n]
