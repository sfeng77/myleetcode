# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a not in d1:
                if b in d2:
                    return False
                d1[a] = b
                d2[b] = a
            else:
                if b != d1[a]:
                    return False
        return True
