class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        solution=[]

        def backtrack(index, cur_sum):
            if index>=len(nums) or cur_sum>target:
                return
            if cur_sum == target:
                res.append(solution.copy())
                return
            solution.append(nums[index])
            backtrack(index, cur_sum+nums[index])
            solution.pop()
            backtrack(index+1, cur_sum)

        backtrack(0,0)
        return res

