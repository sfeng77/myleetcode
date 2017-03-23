# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []

        def evl(a, b, t):
            if t == "+":
                return a + b
            elif t == '-':
                return a - b
            elif t == '*':
                return a * b
            else:
                if a * b < 0 and a % b != 0:
                    return (a / b + 1)
                else:
                    return a / b

        for t in tokens:
            if t in '+-*/':
                a = st.pop()
                b = st.pop()
                c = evl(b,a,t)
                st+=[c]
            else:
                st+=[int(t)]
        return st.pop()
