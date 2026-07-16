class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        drs=[[-1,0],[1,0],[0,1],[0,-1]]
        visited=set()

        def backtrack(i, r, c):
            if i==len(word):
                return True
            
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited or board[r][c]!=word[i]:
                return False

            visited.add((r,c))
            for dr,dc in drs:
                nr,nc = r+dr,c+dc
                if backtrack(i+1, nr, nc):
                    return True
            visited.remove((r,c))    
            return False

        for r in range(ROWS):
            for c in range (COLS):
                if backtrack(0,r,c):
                    return True
        return False
