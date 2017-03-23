class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        List = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        if n<10:
            return List[n-1]
        N2=6
        N3=4
        N5=2
        V2=List[N2]*2
        V3=List[N3]*3
        V5=List[N5]*5
        CM=12
        i=10
        while (i<n):
            while V2<=CM:
                N2+=1
                V2=List[N2]*2
            while V3<=CM:
                N3+=1
                V3=List[N3]*3
            while V5<=CM:
                N5+=1
                V5=List[N5]*5
            VN = min(V2,V3,V5)
            List.append(VN)
            CM = VN
            i+=1
        return CM
