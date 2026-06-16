class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l=0
        r=l+1
        maxP=0

        while l<r and r<n:
            if prices[l]<prices[r]:
                maxP = max(maxP, prices[r]-prices[l])
            else:
                l=r
            r+=1

        return maxP