class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        res=[]

        def backtrack():
            if len(solution)==len(nums):
                res.append(solution[:])
                return
             

            for num in nums:
                if num not in solution:
                    solution.append(num)
                    backtrack()
                    solution.pop()
            
        
        backtrack()
        return res