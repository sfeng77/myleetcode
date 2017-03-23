"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".b

https://leetcode.com/problems/shortest-palindrome/

"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPanlindrom(s):
            if s == s[::-1]:
                return True
            else:
                return False

        for i in range(len(s)-1, 0, -1):
            if s[i] == s[0] and isPanlindrom(s[:i+1]):
                return s[i+1:][::-1]+s
        return s[1:][::-1]+s
