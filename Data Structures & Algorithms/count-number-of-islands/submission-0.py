class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        q = []
        
        def bfs(grid):
            while q:
                for i in range(len(q)):
                    r,c = q.pop(0)
                    directions = [[0,1],[1,0],[0,-1],[-1,0]]
                    for dr,dc in directions:
                        row,col = dr+r,dc+c
                        if (row,col) not in visited:
                            if (row==len(grid)or row<0 or col==len(grid[0])or col<0 or grid[row][col]=='0'):
                                continue
                            q.append([row,col])
                            visited.add((row,col))
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visited:
                    q.append([i,j])
                    bfs(grid)
                    visited.add((i,j))
                    count+=1
        return count