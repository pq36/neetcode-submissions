class Solution:
    def dfs(self,i,j,vis,grid):
        vis[i][j]=True
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        for dx,dy in dir:
            x=i+dx
            y=j+dy
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]=='1' and vis[x][y]==False:
                self.dfs(x,y,vis,grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        vis = [[False] * c for _ in range(r)]  
        res=0
        for i in range(r):
            for j in range(c):
                if vis[i][j]==False and grid[i][j]=='1':
                    self.dfs(i,j,vis,grid)
                    res+=1
        return res


        

        