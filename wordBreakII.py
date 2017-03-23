# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
#

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        import heapq
        ws = set(wordDict)
        letterSetString = set(s)
        letterSetWords = set([])
        for w in ws:
            letterSetWords.update(set(w))
        if not letterSetString <= letterSetWords:
            return []
        #print ws
        n= len(s)
        if n == 0 or len(ws) == 0:  return []
        MAXLEN = max([len(w) for w in wordDict])
        dp = [[] for _ in range(n + 1)]

        front = [0]

        while(front):
            #print front
            i = heapq.heappop(front)
            while(front and i == front[0]):
                heapq.heappop(front)
            #print front
            for j in range(i, min(i + MAXLEN, n)):
                #print i, j
                #print s[i:j+1]
                if s[i:j+1] in ws:
                    if j < n:
                        heapq.heappush(front, j + 1)
                    if i:
                        for p in dp[i]:
                            dp[j+1] += [p + [i]]
                    else:
                        dp[j+1] += [[0]]
                    #print dp

        def listToString(l):
            r = s
            for i in l[:0:-1]:
                r = r[:i]+" "+r[i:]
            return r

        return [listToString(l) for l in dp[n]]
