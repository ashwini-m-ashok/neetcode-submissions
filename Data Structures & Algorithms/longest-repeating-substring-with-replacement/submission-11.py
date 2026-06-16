class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        maxlen=0
        l=0
        maxF=0
        count = defaultdict(int)

        for r in range(n):
            count[s[r]]+=1
            maxF = max(maxF,count[s[r]])

            if ((r-l+1) - maxF)>k:
                count[s[l]]-=1
                l+=1
                
                if maxF == count[s[l]]:
                    maxF-=1
            else:
                maxlen = max(maxlen,r-l+1)

        return maxlen
        

