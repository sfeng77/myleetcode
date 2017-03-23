class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vList1=map(int,version1.split('.'))
        self.deleteTralingZero(vList1)
        vList2=map(int,version2.split('.'))
        self.deleteTralingZero(vList2)
        if vList1>vList2:
            return 1
        elif vList1<vList2:
            return -1
        else:
            return 0

    def deleteTralingZero(self,vList):
        while(len(vList)>0 and vList[-1]==0):
            vList.pop()

    
