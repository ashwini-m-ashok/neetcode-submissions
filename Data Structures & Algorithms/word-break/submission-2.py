class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Say i=6, w="code" (length 4), on s="leetcode" (n=8). i+len(w) = 10, which is > n=8. First, the slice check: s[6:10] → Python clamps this to s[6:8], giving "de". Is "de" == "code"? No. The and short-circuits — since the first condition is False, dfs(10) never gets called at all.

        n=len(s)
        memo={}

        def dfs(i):
            if i==n:
                return True

            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if i+len(w)<=n and s[i:i+len(w)]==w:
                    if dfs(i+len(w)):
                        memo[i]=True
                        return True
            memo[i]=False
            return False
        
        return dfs(0)