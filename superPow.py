#  Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
#
# Example1:
#
# a = 2
# b = [3]
#
# Result: 8
#
# Example2:
#
# a = 2
# b = [1,0]
#
# Result: 1024


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        a = a % 1337
        c = 1
        res = 1
        for d in b[::-1]:
            for i in range(1,11):
                c = c * a % 1337
                if i == d:
                    res = res * c % 1337
            a = c
            c = 1
        return res
