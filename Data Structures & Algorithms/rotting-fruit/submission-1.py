class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq=deque()
        fresh_count=0

        ROWS = len(grid)
        COLS = len(grid[0])
        mins=0
        drs = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_count+=1
                elif grid[r][c]==2:
                    dq.append((r,c))
        
        while fresh_count and dq:
            for _ in range(len(dq)):  
                r,c = dq.popleft()
                for dr, dc in drs:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        dq.append((nr,nc))
                        fresh_count-=1
            
            mins+=1
        
        return mins if fresh_count==0 else -1
                

        