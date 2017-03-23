#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        i = 0
        j = 0
        dp[0][0] = True
        for j in range(m):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]
                for i in range(n):
                    dp[i+1][j+1] = (dp[i+1][j-1]) or (dp[i][j+1] and (p[j-1]=='.' or p[j-1] == s[i]))
            elif p[j] == '.':
                for i in range(n):
                    dp[i+1][j+1] = dp[i][j]
            else:
                for i in range(n):
                    dp[i+1][j+1] = dp[i][j] and (s[i] == p[j])

        return dp[n][m]
