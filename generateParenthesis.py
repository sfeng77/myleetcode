'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

#ACCEPTED

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return []

        def generate(l, r):
            if l > r or l < 0:
                return []
            if l == 0:
                return [")"*r]

            return ['('+p for p in generate(l - 1, r)] + [')'+p for p in generate(l , r - 1)]

        return ["("+p for p in generate(n-1,n)]
