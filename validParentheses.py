"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        closep ={')':'(', '}':'{',']':'['}
        for c in s:
            if c in ['(','{','[']:
                st.append(c)
            else:
                if (not st) or (st.pop() != closep[c]):
                    return False
        return not st
