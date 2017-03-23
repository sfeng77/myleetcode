"""
 Given a positive integer n and you can do operations as follow:

    If n is even, replace n with n/2.
    If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

"""

#BFS

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        pool = {n}
        moves = 0
        while pool:
            newX = set()
            for x in pool:
                if x == 1: return moves
                if (x % 2):
                    newX.add(x + 1)
                    newX.add(x - 1)
                else:
                    newX.add(x / 2)
            pool |= newX
            moves += 1
