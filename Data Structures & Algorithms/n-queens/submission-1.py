class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for r in range(n)] for c in range(n)]
        anti_diagonals= set()
        diagonals=set()
        res=[]
        cols=set()

        def backtrack(r):
            if r>=n :
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or r+c in diagonals or r-c in anti_diagonals:
                    continue
                cols.add(c)
                diagonals.add(r+c)
                anti_diagonals.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                cols.remove(c)
                diagonals.remove(r+c)
                anti_diagonals.remove(r-c)
                board[r][c] = '.'
        
        backtrack(0)
        return res


