class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_pali(l,r):
            res=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                res+=1
            return res
        
        result=0
        for i in range(len(s)):
            result+=count_pali(i,i)
            result+=count_pali(i,i+1)
        return result

            