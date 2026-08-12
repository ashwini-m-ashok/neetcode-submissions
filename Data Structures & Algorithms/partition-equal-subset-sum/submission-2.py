class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        n = len(nums)
        if total%2!=0:
            return False

        def dfs(i, need):
            if i>=len(nums):
                return need==0
            if need<0:
                return False
            
            return dfs(i+1, need-nums[i]) or dfs(i+1, need)

        return dfs(0, total//2)
