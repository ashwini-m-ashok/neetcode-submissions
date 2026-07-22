class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = float('-inf')
        drs = [(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(r, c)->int:
            if r<0 or r>=ROWS or c<0 or c>= COLS or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            area=0
            for dr , dc in drs:
                nr, nc = r+dr, c+dc
                area+=dfs(nr, nc)
            return area+1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
                    

        return res if res != float('-inf') else 0