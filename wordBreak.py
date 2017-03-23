# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        ws = set(wordDict)
        d = {}

        def breakWord(s, ws):
            #print s
            n = len(s)
            if n == 0:  return True
            if s in d:  return False
            for i in range(1,n+1):
                w = s[:i]
                if w in ws and breakWord(s[i:],ws):
                    return True
            d[s] = False
            return False

        return breakWord(s, ws)
