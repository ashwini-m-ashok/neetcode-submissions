class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        solution=[]
        result=[]


        def backtrack(openN, closeN):
            if openN==n and closeN==n:
                result.append(''.join(solution))
                return
            
            if openN<n:
                solution.append('(')
                backtrack(openN+1, closeN)
                solution.pop()
            
            
            if closeN<openN:
                solution.append(')')
                backtrack(openN, closeN+1)
                solution.pop()


        backtrack(0,0)
        return result