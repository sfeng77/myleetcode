class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        if l==0:
            return 0
        maxLen=1
        i=0
        j=1
        subStr=[s[i]]
        while i<l-1:
            lenSubStr=1
            while(j<l and s[j] not in subStr):
                subStr.append(s[j])
                j+=1
            lenSubStr=len(subStr)
            maxLen=max(maxLen,lenSubStr)
            print subStr
            if j==l:
                return maxLen
            while s[i]!=s[j]:
                i+=1
            i+=1
            subStr=list(s[i:j])
        return maxLen
