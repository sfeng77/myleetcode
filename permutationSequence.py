# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
#
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
        digits = range(1,10)
        s = ""
        while(k > 1):
            for i in range(n, 0, -1):
                print k,i,fact[i]
                if k > fact[i]:
                    k -= fact[i]
                    s += str(digits[i-1])
                    digits.pop(i-1)
                    break
        return s + str(digits[0])
