"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".

"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        if(numerator < 0) and (denominator < 0):
            return self.fractionToDecimal(-numerator, - denominator)
        elif numerator < 0:
            return "-"+self.fractionToDecimal(-numerator, denominator)
        elif denominator < 0:
            return "-"+self.fractionToDecimal(numerator, -denominator)

        dn = {}
        dec = []
        count = 0

        result = str(numerator / denominator)
        numerator = numerator % denominator
        if numerator == 0:
            return result
        else:
            result += '.'
        while (numerator not in dn and numerator != 0):
            count += 1
            dn[numerator] = count
            numerator *= 10
            dec.append(str(numerator / denominator))
            numerator = numerator % denominator

        if numerator == 0:
            return result + "".join(dec)
        else:
            idx = dn[numerator]
            result += "".join(dec[:dn[numerator]-1]) + "(" + "".join(dec[dn[numerator]-1:])+")"
            return result
