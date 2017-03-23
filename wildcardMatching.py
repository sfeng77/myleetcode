"""

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false

"""
#accepted

class Solution(object):

    def __init__(self):
        self.d = {}

    def cutMeat(self,p):
        p = p+"*"
        maxLen, currLen, maxId, currId, i = [0] * 5
        while (i < len(p)):
#            print p[i], currLen, maxLen, currId, maxId
            if p[i] == "*":
                if currLen > maxLen:
                    maxLen = currLen
                    maxId = currId
                currLen = 0
            else:
                if currLen == 0:
                    currId = i
                currLen += 1
            i += 1
        return maxId, maxLen


    def isMatchQ(self, s, p):
        if len(s) != len(p):
            return False
        for i in range(len(s)):
            if p[i] != '?' and s[i]!=p[i]:
                return False
        return True

    def cleanStar(self, p):
        l = ""
        for c in p:
            if not l or c!= "*" or l[-1] != "*":
                l+=c
        return l

    def isMatchS(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print s, p

        if not s:
            return (not p) or (p == "*")
        if not p:
            return False
        if p == "*":
            return True

        if len(s)< len(p) - p.count("*"):
            return False

        if p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        #if p[0] != '*':
        #    return (s[0] == p[0]) and self.isMatch(s[1:], p[1:])

        if (s,p) in self.d:
            return self.d[(s,p)]

        maxId, maxLen = self.cutMeat(p)
        head = p[:maxId]
        tail = p[maxId+maxLen:]
        meat = p[maxId:maxId+maxLen]
        #print head, tail, meat

        for i in range(0,len(s) - maxLen + 1):
            #print s[i:i+maxLen]
            if self.isMatchQ(s[i:i+maxLen], meat) and self.isMatchS(s[:i], head) and self.isMatchS(s[i+maxLen:], tail):
                self.d[(s,p)] = True
                return True
        self.d[(s,p)] = False
        return False

    def isMatch(self, s, p):
        return self.isMatchS(s, self.cleanStar(p))
