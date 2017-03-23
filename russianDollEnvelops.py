# You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
#
# What is the maximum number of envelopes can you Russian doll? (put one inside other)
#
# Example:
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        n = len(envelopes)

        if n < 2:
            return n
        envelopes.sort(key = lambda x: x[0])
        myDoll = [1] * n
        myMax = 1
        for i in range(n-1):
            w, h = envelopes[i]
            d = myDoll[i]
            for j in range(i+1, n):
                if envelopes[j][0] > w and envelopes[j][1] > h:
                    myDoll[j] = max(myDoll[j], d + 1)
                    myMax = max(myMax, myDoll[j])

        return myMax
