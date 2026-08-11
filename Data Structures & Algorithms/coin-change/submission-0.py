class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[math.inf]*(amount+1)
        dp[0] = 0

        for amt in range(1,amount+1):
            for val in coins:
                if amt-val>=0:
                    dp[amt] = min(dp[amt],1+dp[amt-val])

        return dp[amount] if dp[amount]!=math.inf else -1