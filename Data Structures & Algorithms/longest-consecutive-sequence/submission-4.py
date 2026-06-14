class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len =0

        for num in nums:
            if num-1 not in nums_set:
                    
                streak = 1
                while num+streak in nums_set:
                    streak+=1
                max_len = max(max_len, streak)
        
        return max_len
