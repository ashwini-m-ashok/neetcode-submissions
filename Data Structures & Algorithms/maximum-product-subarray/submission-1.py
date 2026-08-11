class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cur_min , cur_max = 1, 1
        result = nums[0]
        for num in nums:
            options = (num, cur_max*num, cur_min*num)
            cur_max = max(options)
            cur_min = min(options)
            
            result = max(result, cur_max)
        
        return result