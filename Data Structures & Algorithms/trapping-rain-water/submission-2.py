class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        n = len(height)
        maxR = height[n-1]
        total = 0
        r= n-1
        l=0

        while l<r:
            if maxL<maxR:
                l+=1
                maxL = max(maxL, height[l])
                total+= maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                total+= maxR-height[r]
        
        return total
