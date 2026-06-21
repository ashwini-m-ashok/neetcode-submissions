class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        n=len(piles)
        r=max(piles)

        while l<r:
            mid = (l+(r-l)//2)
            total_hours=0
            for pile in piles:
                total_hours+= math.ceil(pile/mid)
            
            if total_hours>h:
                l = mid+1
            elif total_hours<=h:
                r=mid
        return r



