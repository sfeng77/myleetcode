# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#http://www.leetcode.com/wp-content/uploads/2012/04/histogram.png
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#http://www.leetcode.com/wp-content/uploads/2012/04/histogram_area.png
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        n = len(heights)
        res = heights[0]
        for i in range(n):
            if i > 0 and heights[i] <= heights[i-1]:
                continue
            partialMin = heights[i]
            for j in range(i, n):
                if heights[j] < partialMin:
                    partialMin = heights[j]
                A = partialMin * (j-i+1)
                #print i, j, partialMin, A
                if A > res:
                    res = A
        return res
