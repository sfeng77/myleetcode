#  A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        num = [1] * n
        singleDigit = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        def single(c):
            return singleDigit[int(c)]

        def double(s):
            a = int(s)
            if 0 <= a <= 9 or a > 26:
                return 0
            else:
                return 1

        if n == 0:
            return 0

        if n == 1:
            return single(int(s))

        num[0] = single(s[-1])
        num[1] = single(s[-2]) * num[0] + double(s[-2:])

        for i in range(2,n):
            num[i] = single(s[-(i+1)]) * num[i-1] + double(s[-(i+1):-(i-1)]) * num[i-2]

        return num[n-1]
