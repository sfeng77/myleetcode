#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
#     Only one letter can be changed at a time.
#     Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
#
#     Return 0 if there is no such transformation sequence.
#     All words have the same length.
#     All words contain only lowercase alphabetic characters.
#     You may assume no duplicates in the word list.
#     You may assume beginWord and endWord are non-empty and are not the same.


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        front = set([beginWord])
        back = set([endWord])
        wl = len(beginWord)
        wordList = set(wordList)
        if (back & wordList == set()):  return 0
        ladderLen = 1
        wordList.discard(beginWord)
        while(front):
            print front, back
            if front & back :
                return ladderLen
            front = wordList & set([s[:i]+c+s[i+1:] for s in front for i in range(wl) for c in 'abcdefghijklmnopqrstuvwxyz'])
            if len(front) > len(back):
                back, front = front, back
            ladderLen += 1
        return 0
