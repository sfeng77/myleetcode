"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def cutIP(s, n):
            if n > len(s):
                return []
            if n == 1:
                v = int(s)
                if v > 255 or (v > 0 and s[0] == '0') or (v == 0 and len(s) > 1) :
                    return []
                else:
                    return [s]
            myIP = []

            if s[0] == '0':
                maxSegLen = 1
            else:
                maxSegLen = min(len(s) - n + 1, 3)
            for i in xrange(1, maxSegLen + 1):
                seg = int(s[:i])
                if seg < 256:
                    myIP += [s[:i] + "." + p for p in cutIP(s[i:], n - 1)]

            return myIP

        return cutIP(s, 4)
