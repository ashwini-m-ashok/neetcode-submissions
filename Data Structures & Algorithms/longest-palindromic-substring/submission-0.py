class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==1:
            return s
        if n==2:
            return s[0] if s[0]!=s[1] else s
        res_len = -float('inf')
        res=''
        
        def pal_length(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                    l-=1
                    r+=1
            return [l+1,r-1]
        
        for i in range(n-1):
            l1,r1 = pal_length(i,i+1)
            l2,r2 = pal_length(i,i)
            lmax=l1
            rmax=r1

            if (r2-l2)>(r1-l1):
                lmax=l2
                rmax=r2
            if res_len < (rmax-lmax):
                res_len =  (rmax-lmax)
                res = s[lmax:rmax+1]
        
        return res

