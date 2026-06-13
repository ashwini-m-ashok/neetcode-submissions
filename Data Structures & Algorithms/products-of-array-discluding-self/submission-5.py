class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_prefix = [1]*n
        product_suffix = [1]*n
        output = [1]*n

        for i in range(1,n):
            product_prefix[i] = product_prefix[i-1]*nums[i-1]

        for i in range(n-2, -1,-1):
            product_suffix[i] = product_suffix[i+1]*nums[i+1]

        for i in range(n):
            output[i] = product_prefix[i]*product_suffix[i]
        
        return output

