"""
Follow up for H-Index: What if the citations array is sorted in ascending order?
Could you optimize your algorithm?
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        i = 0
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] + mid >= n:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
