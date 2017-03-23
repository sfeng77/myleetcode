# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        mylist = []
        for c in digits[::-1]:
            s = c + carry
            if s > 9:
                s -= 10
                carry = 1
            else:
                carry = 0
            mylist = [s] + mylist
        if carry:
            mylist = [1] + mylist
        return mylist
