#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Solution():
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count("A") < 2 and "LLL" not in s

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        if n == 0:
            return ""
        if n == 1:
            return str(nums[0])
        if n == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            return str(nums[0]) + "/(" + "/".join(str(i) for i in nums[1:]) + ")"

    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        for i in range(n):
            s = strs[i]
            if s < s[::-1]:
                strs[i] = s[::-1]

        js = "".join(strs)
        maxc = max(js)
        opts = []
        for i in range(n):
            s = strs[i]
            if maxc not in s:
                continue
            ls = len(s)
            for j in range(ls):
                if s[j] == maxc:
                    opt1 = s[j:] + "".join(strs[i+1:]) + "".join(strs[:i]) + s[:j]
                    opt2 = s[j::-1] + "".join(strs[i+1:]) + "".join(strs[:i]) + s[:j:-1]
                    opts.append(opt1)
                    opts.append(opt2)
        return max(opts)
