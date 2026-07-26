class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dq=deque()
        grid=heights
        ROWS = len(grid)
        COLS = len(grid[0])
        
        drs = [(-1,0),(1,0),(0,-1),(0,1)]
        pac=set()
        atl=set()

        def dfs(r, c, visited): 
            visited.add((r,c))
                 
            for dr, dc in drs:
                nr,nc=r+dr, c+dc
                if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,visited)


        for r in range(ROWS):
            dfs(r,0,pac)        
        for c in range(COLS):
            dfs(0, c,pac )

        for r in range(ROWS):
            dfs(r, COLS-1, atl)
        for c in range(COLS):
            dfs(ROWS-1,c, atl)
        
        return list(pac&atl)

                        
