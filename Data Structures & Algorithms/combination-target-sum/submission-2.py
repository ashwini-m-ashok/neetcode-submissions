class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        solution=[]

        def bt(i):
            if sum(solution)>target or i>= len(nums):
                return
            if sum(solution)==target:
                res.append(solution[:])
                return
            
            solution.append(nums[i])
            bt(i)

            solution.pop()
            bt(i+1)
        
        bt(0)
        return res
