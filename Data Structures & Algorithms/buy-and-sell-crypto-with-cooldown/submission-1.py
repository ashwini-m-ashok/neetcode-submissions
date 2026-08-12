class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp={}

        def dfs(i, buying):
            if i>=n:
                return 0

            if (i, buying) in dp:
                return dp[(i,buying)]

            cooldown = dfs(i+1,buying)

            if buying:
                buy_profit = dfs(i+1, not buying) - prices[i]
                dp[(i,buying)] = max(buy_profit, cooldown)
            else:
                sell_profit = dfs(i+2, not buying) + prices[i]
                dp[(i,buying)] = max(sell_profit, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)
            

