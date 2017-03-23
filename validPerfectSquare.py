"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True

Example 2:

Input: 14
Returns: False

"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num in [0, 1]: return True
        l = 1
        r = num - 1
        while(l < r):
            m = (l + r ) / 2
            if m * m == num:
                return True
            elif m * m > num:
                r = m
            else:
                l = m + 1
        return False
