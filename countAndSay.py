"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def say(s):
            if s == "": return ""
            c = s[0]
            n = 1
            while(n<len(s) and s[n] == c):
                n += 1
            return str(n)+c+say(s[n:])

        s = '1'
        for i in range(1, n):
            s = say(s)
        return s
