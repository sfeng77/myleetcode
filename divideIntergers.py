# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return MAX_INT
        if dividend == 0:
            return 0
        positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        partialSum = 0
        res = 0
        for i in range(31, -1,  -1):
            if (partialSum + (divisor << i)) <= dividend:
                res += (1<< i)
                partialSum += (divisor << i)
                #print partialSum, res
        if positive:
            return min(0x7FFFFFFF,res)
        else:
            return - res
