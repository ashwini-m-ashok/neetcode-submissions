class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(m):
            for c in range(n):
                cur = board[r][c]
                if cur!='.' and cur not in rows[r] and cur not in cols[c] and cur not in squares[(r//3,c//3)]:
                    rows[r].add(cur)
                    cols[c].add(cur)
                    squares[(r//3,c//3)].add(cur)
                elif cur!='.':
                    return False
        return True
