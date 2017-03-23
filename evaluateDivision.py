# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
#
# According to the example above:
#
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
#

#UNION FIND
class Solution(object):
    def __init__(self):
        self.leader = {}
        self.members = {}
        self.values = {}

    def addToGroup(self, equation, value):
        a, b = equation
        if a in self.leader and b in self.leader:
            la = self.leader[a]
            lb = self.leader[b]
            if la != lb:
                value *= self.values[b] / self.values[a]
                # va = a / la, vb = b / lb, va / vb = v
                # la / lb = (a / va) / (b / vb) = vb /va * b/a = vb / va * v
                lena = len(self.members[la])
                lenb = len(self.members[lb])
                if lena < lenb:
                    la, lb = lb, la
                    value = 1.0 / value
                self.mergegroup(la, lb, value)

        elif a not in self.leader and b not in self.leader:
            self.leader[a] = a
            self.leader[b] = a
            self.members[a] = {a, b}
            self.values[a] = 1.0
            self.values[b] = 1.0 / value

        else:
            if a in self.leader:
                a, b = b, a
                value = 1.0 / value
            l = self.leader[b]
            self.leader[a] = l
            self.members[l] |= {a}
            self.values[a] = self.values[b] * value


    def mergegroup(self, leaderA, leaderB, value):
        #print "Merging group " + leaderA +" with group " + leaderB
        #print "value = " + str(value)
        for m in self.members[leaderB]:
            self.values[m] /= value
            self.leader[m] = leaderA
            self.members[leaderA] |= {m}
        self.members.pop(leaderB)

    def evaluate(self, a, b):
        if a in self.leader and b in self.leader and self.leader[a] == self.leader[b]:
            return self.values[a] / self.values[b]
        else:
            return - 1.0

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        for e, v in zip(equations, values):
            self.addToGroup(e,v)

        res = []
        for a, b in queries:
            res += [self.evaluate(a, b)]
        return res
