class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        sortedCite = citations
        sortedCite.sort()
        N = len(citations)
        i = 0 ;
        while (i<N and sortedCite[N-1-i] > i and sortedCite[N-1-i]>0):
            #print i, sortedCite[N-1-i]
            i+=1
        return i
