class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_index = dict()

        for i in range(len(nums)):
            num = nums[i]
            if num in diff_to_index:
                return [diff_to_index[num],i]
            diff = target-num
            diff_to_index[diff] = i
        
        return []