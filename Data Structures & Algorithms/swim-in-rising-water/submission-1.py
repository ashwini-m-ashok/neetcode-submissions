class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = defaultdict(list)
        minheap=[[grid[0][0],0,0]]
        ROWS,COLS = len(grid), len(grid[0])

        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited.add((0,0))

        while minheap:
            height , r,c = heapq.heappop(minheap)

            if r==ROWS-1 and c==COLS-1:
                return height
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=ROWS or nc<0 or nc>= COLS or (nr,nc) in visited:
                    continue

                visited.add((nr,nc))
                heapq.heappush(minheap,[max(height,grid[nr][nc]), nr,nc])
        