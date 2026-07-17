class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        solution=[]

        def backtrack(i):
            if i>=len(digits):
                if len(solution)>0:
                    res.append(''.join(solution))
                return
            
            cur_num = mapping[digits[i]]
            for j in range(len(cur_num)):
                solution.append(cur_num[j])
                backtrack(i+1)
                solution.pop()

        backtrack(0)
        return res