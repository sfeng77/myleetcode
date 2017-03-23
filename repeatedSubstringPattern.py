# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
#
# Example 1:
#
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
#
# Example 2:
#
# Input: "aba"
#
# Output: False
#
# Example 3:
#
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        n = len(str)

        if n < 2:
            return False

        count = [str.count(c) for c in set(str)]
        d = len(count)

        if d == 1:
            return True

        def gcd(a,b):
            if a < b:
                a, b = b, a
            while(b):
                a, b = b, a % b
            return a

        r = gcd(count[0], count[1])
        if d > 2:
            for i in range(2, d):
                r = gcd(r, count[i])

        for i in range(2, r + 1):
            if r % i == 0 and str[:n/i] * i == str:
                return True

        return False
