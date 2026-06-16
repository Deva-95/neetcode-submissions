class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = []
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
        while(q and fresh):
            
            for i in range(len(q)):
                r,c = q.pop(0)
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    row,col = dr+r,dc+c
                    if (row==len(grid)or row<0 or col==len(grid[0])or col<0 or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    fresh-=1
                    q.append([row,col])
            time+=1
        return time if not fresh else -1