class Solution(object):
    def getTrapLevel(self,height,level):
        #find the amount of water trapped in a specific level
        N = len(height)
        leftClosed = False
        hole = 0
        water = 0
        for i in range(N):
            if leftClosed == False:
                if height[i] >= level:
                    leftClosed = True
            else:
                if height[i]<level:
                    hole +=1
                else:
                    water += hole
                    hole =0
        return water

    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        pool = 0
        heightSet=list(set(height))
        heightSet.sort()
        base = 0
        for l in heightSet:
            #print l
            pool += (l-base)*self.getTrapLevel(height, l)
            base = l
        return pool


    def easyTrap(self,height):
        water = 0 ;
        for i in range(1,len(height)-1):
            column = min(max(height[:i]),max(height[i:]))-height[i]
            water += (column >0) * column
        return water


    def turboTrap(self,height):
        N=len(height)
        leftBar=[0]*N
        rightBar=[0]*N
        maxLeft=0
        maxRight=0
        for i in range(0,N):
            maxLeft=max(maxLeft,height[i])
            leftBar[i]=maxLeft
            
        for i in range(N-1,-1,-1):
            maxRight=max(maxRight,height[i])
            rightBar[i]=maxRight
        
        water = 0
        for i in range(1,N-1):
            column = min(leftBar[i-1],rightBar[i+1])-height[i]
            water += (column >0) * column
        return water
            

