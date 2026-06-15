class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n=len(heights)
        r=n-1
        max_area = 0

        while l<r:
            max_area = max(max_area, min(heights[l],heights[r])*(r-l))
            if heights[l]>=heights[r]:
                r-=1
            else:
                l+=1
        
        return max_area
