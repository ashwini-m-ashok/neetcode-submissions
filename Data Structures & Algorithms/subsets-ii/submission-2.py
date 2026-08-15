class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        solution=[]
        nums.sort()
        def backtrack(index):
            if index ==len(nums):
                res.append(solution.copy())
                return
            solution.append(nums[index])
            backtrack(index+1)

            solution.pop()

            while index+1<len(nums) and nums[index+1]==nums[index]:
                index+=1
            backtrack(index+1)
            
        backtrack(0)
        return res