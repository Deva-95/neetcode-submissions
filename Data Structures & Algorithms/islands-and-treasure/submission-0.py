class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        q = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j])
                    visit.add((i, j))
        
        dist = 0
        while q:

            for i in range(len(q)):

                r,c  = q.pop(0)
                grid[r][c] = dist
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    row,col = dr+r,dc+c
                    if (row,col) not in visit:
                        if (row==len(grid)or row<0 or col==len(grid[0])or col<0 or grid[row][col]==-1):
                            continue
                        visit.add((row, col))
                        q.append([row,col])
            dist+=1
        return 