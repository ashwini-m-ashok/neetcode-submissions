class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        solution=[]

        def backtrack(index):
            if index==len(nums):
                res.append(solution.copy())
                return
            solution.append(nums[index])
            backtrack(index+1)

            solution.pop()
            backtrack(index+1)
            
        backtrack(0)
        return res