
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        for w in range(int(sqrt(area)), 0, -1):
            if area % w == 0:
                return [area / w, w]
