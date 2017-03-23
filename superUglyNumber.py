#  Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
#

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        l = [1]
        np = len(primes)
        pId = [1] * np
        candidates = zip(primes,range(np))
        heapq.heapify(candidates)
        lastAdded = 1
        i = 0
        while(i<n):
            #print candidates, pId, l
            c, p = heapq.heappop(candidates)
            if c != l[-1]:
                l += [c]
                i += 1
            heapq.heappush(candidates, (primes[p] * l[pId[p]], p ))
            pId[p] += 1
        #print l
        return l[n-1]
