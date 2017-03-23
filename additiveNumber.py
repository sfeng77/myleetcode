#  306. Additive Number
#
# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
#
# For example:
# "112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
#
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
# "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
#
# 1 + 99 = 100, 99 + 100 = 199
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
#
# Follow up:
# How would you handle overflow for very large input integers?


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def toInt(num):
            return int(num)

        def isAdditive(num, a, b):
            print num, a, b
            s = a + b
            m = len(str(s))
            n = len(num)
            if toInt(num[:m]) == s:
                if m == n:
                    return True
                else:
                    return isAdditive(num[m:], b, s)
            else:
                return False

        n = len(num)
        for p in range(n/2, 0, -1):
            a = toInt(num[:p])
            if num[0] == '0' and p > 1:
                continue
            for q in range(p + (n - p) / 2, p , -1):
                if num[p] == '0' and q!= p + 1:
                    continue
                b = toInt(num[p:q])
                if num[q]=='0' and a + b != 0:
                    continue
                #print b
                if isAdditive(num[q:], a, b):
                    return True
        return False
