class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=0
        n = len(nums)
        r=n-1
        nums.sort()
        output=[]

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue

            need = -nums[i]
            l=i+1
            r=n-1

            while l<r:
                total = nums[l]+nums[r]

                if total==need:
                    output.append([nums[i],nums[l],nums[r]])
                    while r>0 and nums[r]==nums[r-1]:
                        r-=1
                    while l<n-1 and nums[l]==nums[l+1]:
                        l+=1
                    
                    r-=1
                    l+=1
                elif total>need:
                        r-=1
                else:
                    l+=1
        return output