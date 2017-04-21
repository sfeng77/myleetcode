# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        n = len(intervals)
        if n <= 1:
            return intervals

        ints = sorted([(i.start, i.end) for i in intervals])
        s, e = ints[0]
        res = []
        for (a, b) in ints[1:]:
            if b <= e:
                continue

            if a > e:
                res.append(Interval(s, e))
                s = a

            e = b

        res.append(Interval(s, e))
        return res
