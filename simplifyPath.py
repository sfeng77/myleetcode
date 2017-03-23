'''

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        p =[d for d in path.split('/') if d and d!='.']
        wd = []
        for d in p:
            if d == '..':
                if wd:
                    wd.pop()
            else:
                wd.append(d)
        return '/'+'/'.join(wd)
