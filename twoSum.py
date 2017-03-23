class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idxList=self.sortNums(nums)
        print idxList
        l=len(idxList)
        for i in range(l):
            firstNum=idxList[i][0]
            left=i
            right=l
            mid=(left+right)/2
            while(right>left+1):
                midValue=idxList[mid][0]
                print left,right,mid,midValue
                if (firstNum+midValue)==target:
                    idx1=idxList[i][1]+1
                    idx2=idxList[mid][1]+1
                    return([min(idx1,idx2),max(idx1,idx2)])
                if (firstNum+midValue)>target:
                    right=mid
                    mid=(left+right)/2
                else:
                    left=mid
                    right=l
                    mid=(left+right)/2


    def sortNums(self,nums):
        numList=list(nums)
        idxList=[]
        l=len(numList)
        print numList
        for i in range(l):
            idxList.append([numList[i],i])
        idxList.sort()
        return idxList
