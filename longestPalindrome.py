# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        length = 0
        for c in s:
            if d.get(c,0) == 0:
                d[c] = 1
            else:
                length += 1
                d[c] = 0
        length *= 2
        for c in d.keys:
            if d[c] > 0:
                length += 1
                break
        return length
