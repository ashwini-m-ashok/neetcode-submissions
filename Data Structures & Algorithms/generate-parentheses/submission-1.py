class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        solution=[]
        res=[]

        def backtrack(openN,closeN):
            if len(solution)==2*n:
                res.append(''.join(solution))
                return

            if openN<n:
                solution.append( '(')
                backtrack(openN+1, closeN)
                solution.pop()

            if openN>closeN:
                solution.append(')')
                backtrack(openN, closeN+1)
                solution.pop()
        backtrack(0,0)
        return res