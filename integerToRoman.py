"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = {1:'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90:'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        romanNum = ''
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        for k in keys:
            while num >= k:
                num -= k
                romanNum += symbols[k]
        return romanNum
