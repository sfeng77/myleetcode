"""
The Skyline Problem

"""
import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        #buildings.sort(key = lambda x:x[0])
        buildingCount = len(buildings)
        if buildingCount == 0:
            return []

        #corners = [[buildings[bid][0],buildings[bid][2],0] for bid in xrange(buildingCount)]
        corners = [[L, H, R] for L, R, H in buildings]
        corners += [[R, None, 0] for L, R, H in buildings]
        #corners += [[buildings[bid][1],buildings[bid][2],1] for bid in xrange(buildingCount)]

        corners.sort()

        skyline = []
        shift = corners[0][0] - 1
        skylineheight = -1
        h=[[0, float("inf")]]

        for c in corners:
            if c[0] > shift:
                while(c[0] > h[0][1]):
                    heapq.heappop(h)
                try:
                    if h[0][0] != skylineheight:
                        skyline.append([shift, -h[0][0]])
                        skylineheight = h[0][0]
                except IndexError:
                    skyline.append([shift,0])
                shift = c[0]

            if c[1]:
                heapq.heappush(h, [- c[1], c[2]])

# not necessary due to the explanation in the method below
#            else:
#                i = h.index(- c[1])
#                h[i] = h[-1]
#                h.pop()
#                heapq.heapify(h)

        skyline.append([shift, 0])
        skyline.pop(0)
        return skyline


    def _getSkyline(self, buildings):
        """
        https://discuss.leetcode.com/topic/34119/10-line-python-solution-104-ms/2
        credit : kitt
        """
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        #print "events:", events
        for x, negH, R in events:
            #print "hp:",hp
            #print "res:", res
            #print "-" * 10
            while x >= hp[0][1]: #???
            # only the highest building matters.
            # as long as it's live
            # no need to worry about the rest of them...
            # fucking brilliant
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]:
                res += [x, -hp[0][0]],
        return res[1:]
