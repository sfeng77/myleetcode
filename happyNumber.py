class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(n!=4):
            if n==1 :return True
            n=sum(int(x)**2 for x in list(str(n)))
        return False
