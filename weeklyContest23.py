#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Solution():

# Reverse String II
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

    def reverseStringII(self,s, k):
        n = len(s)
        res = list(s)
        for start in range(0, (n / (2*k)+1) * 2 * k , 2* k):
            j = min(start + k, n) - 1
            print start, j
            i = start
            while(i < j):
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        return "".join(res)

# Minimum Time Difference
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
#
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.

    def convertToMinute(self, s):
        h= int(s.split(":")[0])
        m= int(s.split(":")[1])
        return h * 60 + m

    def minTimeDifference(self, times):
        mytimes = [self.convertToMinute(s) for s in times]
        mytimes.sort()
        newtimes = mytimes[1:] + [mytimes[0] + 60 * 24]
        timediff = [i-j for i, j in zip(newtimes, mytimes)]
        return min(timediff)


# Construct Binary Tree from String
# You need to construct a binary tree from a string consisting of parenthesis and integers.
#
# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
#
# You always start to construct the left child node of the parent first if it exists.
#
# Example:
# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
#
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
# Note:
# There will only be '(', ')', '-' and '0' ~ '9' in the input string.
# An empty tree is represented by "" instead of "()".

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        n= len(s)
        def parseStr(self, s, i):
            if s[i] == ")":
                return  (i+1, None)
            v = 0
            while(s[i].isdigit):
                v = v* 10 +int(s[i])
                i += 1
            p = TreeNode(v)
            i, p.left = parseStr(s, i + 1)
            i, p.right = parseStr(s, i + 1)
            return i, p

        i, root = parseStr(s, 0)
        return root

# Word Abbreviation
# Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.
#
# Begin with the first character and then the number of characters abbreviated, which followed by the last character.
# If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
# If the abbreviation doesn't make the word shorter, then keep it as original.
# Example:
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# Note:
# Both n and the length of each word will not exceed 400.
# The length of each word is greater than 1.
# The words consist of lowercase English letters only.
# The return answers should be in the same order as the original array.

    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        mydic = {}
        res = {}
        for word in dict:
            abbr = self.findabbrv(word)
            mydic[abbr] = mydic.get(abbr, []) + [word]

        for a in mydic.keys():
            vals = mydic.pop(a)
            if len(vals) == 1:
                res[vals[0]] = a
            else:
                commonprefix = vals[0][0]
                subres = self.wordsAbbreviation([w[1:] for w in vals])
                for w,a in zip(vals,subres):
                    res[w] = commonprefix + a
        return [res[w] for w in dict]


    def findabbrv(self, word):
        n= len(word)
        if n >3:
            return (word[0]+str(n-2) + word[-1])
        else:
            return word
