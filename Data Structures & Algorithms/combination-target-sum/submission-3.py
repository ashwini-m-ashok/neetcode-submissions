class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        solution=[]

        def bt(i, cur_sum):
            if cur_sum>target or i>= len(nums):
                return
            if cur_sum==target:
                res.append(solution[:])
                return
            
            solution.append(nums[i])
            bt(i, cur_sum+nums[i])

            solution.pop()
            bt(i+1, cur_sum)
        
        bt(0,0)
        return res
