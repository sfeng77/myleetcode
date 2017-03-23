#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

class Solution():
# Detect Capital
#
# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
#     All letters in this word are capitals, like "USA".
#     All letters in this word are not capitals, like "leetcode".
#     Only the first letter in this word is capital if it has more than one letter, like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.
#
# Example 1:
#
# Input: "USA"
# Output: True
#
# Example 2:
#
# Input: "FlaG"
# Output: False


    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())

# Beautiful Arrangement
#  Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 ≤ i ≤ N) in this array:
#
#     The number at the ith position is divisible by i.
#     i is divisible by the number at the ith position.
#
# Now given N, how many beautiful arrangements can you construct?
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation:
#
# The first beautiful arrangement is [1, 2]:
#
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
#
# The second beautiful arrangement is [2, 1]:
#
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
#
# Note:
#
#     N is a positive integer and will not exceed 15.


    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        mutation = {}
        for i in range(1, N+1)

# Contiguous Array
#
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
#
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#
# Example 2:
#
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = {}
        c = 0
        d[0] = 0
        l = 0
        for i in range(n):
            if nums[i]:
                c += 1
            else:
                c -= 1
            if c in d:
                l = max(l, i - d[c] + 1)
            else:
                d[c] = i + 1
        return l

# Super Washing Machines II
# You have n super washing machines are arranged in a circle.That means the first washing machine is adjacent to the last one. Initially, each washing machine has some dresses or is empty.
#
# For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time .
#
# Given an integer array represents the number of dresses in each washing machine in the circle, you should find the minimum moves to make all the washing machines have the same number of dresses. If it is not possible to finish it, return -1.
#
# Example1
#
# Input: [0,0,2,2]
#
# Output: 1
#
# Explanation:
# 1st move:     -->  0     0 <-- 2     2    =>    1     1     1     1
#              |_ _ _ _ _ _ _ _ _ _ _ _|
#
# Note:
#
#     The range of n is [1, ???].
#     The range of dresses number in a super washing machine is [0, ???].


# Submission Result: Wrong Answer
# Input: [0,0,11,5]
# Output: 7
# Expected: 8

    def findMinMoves(self, machine):
        """
        :type machine: List[int]
        :rtype: int
        """
        n = len(machine)
        if sum(machine) % n != 0:
            return -1
        target = sum(machine) / n
        return max([abs(m - target) for m in machine])
