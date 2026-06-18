class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n<k:
            return []
        dq = deque()
        output=[]

        for i in range(k):
            while dq and nums[dq[-1]]<= nums[i]:
                dq.pop()
            dq.append(i)
        
        output.append(nums[dq[0]])
        
        for r in range(k,n):   

            while dq and r-dq[0]>=k:
                dq.popleft()

            while dq and nums[dq[-1]]<= nums[r]:
                dq.pop()
            
            dq.append(r)

            if dq:
                output.append(nums[dq[0]])

        return output

            
            

        