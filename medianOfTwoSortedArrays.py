# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m >= n:
            return self.findMedian(nums1, 0, m, nums2, 0, n)
        else:
            return self.findMedian(nums2, 0, n, nums1, 0, m)


    def findMedian(self, nums1, s1, n1, nums2, s2, n2):
        #return median of nums1[s1:s1+n1] + nums2[s2:s2+n2], assuming n1 >= n2
        m1 = self.median(nums1, s1, n1)
        m2 = self.median(nums2, s2, n2)
        #print s1, n1, m1,  s2, n2, m2
        if (n2 == 0):
            return m1

        if (n2 == 1):
            if (n1%2 == 0):
                return self.med3unsorted(m2, nums1[s1+n1/2-1], nums1[s1+n1/2])
            elif n1 == 1:
                return 0.5 * (m1 + m2)
            else:
                return 0.5 * m1 + 0.5 * self.med3unsorted(m2, nums1[s1+n1/2-1], nums1[s1+n1/2 + 1])

        if (n2 == 2):
            b0, b1 = nums2[s2], nums2[s2+1]
            if n1 ==2:
                return self.med4unsorted(nums1[s1],nums1[s1+1], b0, b1)

            if (n1%2 == 0):
                return self.med4unsorted(nums1[s1 + n1/2-1], nums1[s1 + n1/2], max(b0, nums1[s1 + n1/2 -2]), min(b1, nums1[s1+n1/2 + 1]))

            return self.med3unsorted(nums1[s1+n1/2], max(b0, nums1[s1+n1/2-1]), min(b1, nums1[s1+n1/2+1]))

        if m1 == m2:
            return m1
        elif m1 < m2:
            return self.findMedian(nums1, s1 + (n2-1) / 2, n1 - (n2-1) / 2, nums2, s2, n2 - (n2-1) / 2)
        else:
            return self.findMedian(nums1, s1, n1 - (n2-1) / 2, nums2, s2 + (n2-1)/2, n2 - (n2-1) / 2)

    def med3unsorted(self, a, b, c):
        return sorted([a, b, c])[1]

    def med4unsorted(self, a, b, c, d):
        nums = sorted([a, b, c, d])
        return 0.5 * (nums[1] + nums[2])

    def median(self, nums, start, n):
        # returns median of nums[start:start+n]
        if not nums:
            return -1
        if n%2 == 0:
            return 0.5 * (nums[start + n/2] + nums[start + n/2-1])
        else:
            return (nums[start + n/2])
