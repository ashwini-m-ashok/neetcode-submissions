class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        solution=[]
        res=[]
        nums.sort()

        def backtrack(i):
            if i>=len(nums):
                res.append(solution.copy())
                return
            
            solution.append(nums[i])
            backtrack(i+1)
            solution.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1)

        backtrack(0)
        return res