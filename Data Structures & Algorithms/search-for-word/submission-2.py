class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        drs = [[-1,0],[1,0],[0,1],[0,-1]]
        visited=set()

        def dfs(i, r, c):
            if i==len(word):
                return True
            res = False
            if 0<=r<ROWS and 0<=c<COLS and ((r,c) not in visited) and board[r][c]==word[i]:

                visited.add((r,c))
                for dr, dc in drs:
                    nr, nc = r+dr, c+dc
                    if dfs(i+1, nr, nc):
                        res=True
                        break
                visited.remove((r,c))
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0,r,c):
                    return True
        return False



