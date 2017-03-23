# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def isAnagram(w):
            return str(sorted(w))

        d = {}
        for  w in strs:
            k = isAnagram(w)
            d[k] = d.get(k, []) + [w]

        return [d[k] for k in d.keys()]
