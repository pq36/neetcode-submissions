class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rm=set()
        cm=set()
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rm.add(i)
                    cm.add(j)
        for t in cm:
            for i in range(r):
                matrix[i][t]=0
        for t in rm:
            for j in range(c):
                matrix[t][j]=0

        
        
        