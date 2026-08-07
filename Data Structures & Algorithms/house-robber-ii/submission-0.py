class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        def dpp(arr):
            dp=[0]*len(arr)

            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])

            for i in range(2,len(arr)):
                dp[i] = max(arr[i]+dp[i-2],dp[i-1])
        
            return dp[len(arr)-1]


        nums1 = nums[:n-1]
        nums2 = nums[1:]

        return max(dpp(nums1),dpp(nums2))