"""

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13

"""

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        if n < 10: return 1
        s = str(n)
        l = len(s)
        d = int(s[0])
        if n == 10 ** l - 1:
            return l * 10 ** (l - 1)
        if n == 2 * 10 ** (l-1):
            return (10 + 2 * (l-1)) * 10 ** (l - 2)

        if d == 1:
            return self.countDigitOne(10 ** (l - 1) - 1) + 1 + int(s[1:]) + self.countDigitOne(int(s[1:]))
        else:
            return self.countDigitOne(2 * 10 ** (l- 1)) + (d - 2) * self.countDigitOne(10 ** (l - 1) - 1) + self.countDigitOne(int(s[1:]))
