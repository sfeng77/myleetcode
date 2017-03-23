# You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.
#
# If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.
#
# Operations allowed:
#
#     Fill any of the jugs completely with water.
#     Empty any of the jugs.
#     Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
#
# Example 1: (From the famous "Die Hard" example)
#
# Input: x = 3, y = 5, z = 4
# Output: True
#
# Example 2:
#
# Input: x = 2, y = 6, z = 5
# Output: False

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        def gcd(a,b):
            if a < b:
                a, b = b, a
            while(b):
                a, b = b, a % b
            return a

        return z == 0 or (z - x <= y and z % gcd(x, y) == 0);


# Nothing below this line is relevant.

        if x!= 0 and y != 0:
            c = gcd(y, x)
            if z % c != 0:
                return False
            x, y, z = x/c, y/c, z/c

        #print c, x, y, z

        jugA = 0
        jugB = 0
        #visited = [[0] * (y + 1) for _ in range(x + 1)]
        visited = set([])
        newMoves = set([(0,0)])
        while(newMoves):
            a, b = newMoves.pop()
            #print a, b
            if a == z or b == z or a + b == z:    return True
            mymove = [(x,b),(0,b),(a,y),(b,y),(0, a+b), (a + b - y, y), (a + b, 0), (x, a + b - x)]
            newMoves.update([(i,j) for (i,j) in mymove if 0<=i <=x if 0<=j<=y if (i,j) not in visited])
            visited.update([(a, b)])
            print a, b, newMoves
        #print visited
        return False
