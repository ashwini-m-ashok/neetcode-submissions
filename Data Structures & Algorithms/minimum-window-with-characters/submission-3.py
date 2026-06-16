class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''
        
        t_freq = Counter(t)
        window_len = len(t)
        window_freq = {}
        
        need = len(t_freq)
        have = 0

        l=0
        min_len=float("infinity")
        result=''

        for r in range(len(s)):
            window_freq[s[r]] = 1 + window_freq.get(s[r], 0)

            if s[r] in t and window_freq[s[r]] == t_freq[s[r]]:
                have+=1
            
            while have==need:
                if r-l+1 < min_len:
                    result = s[l:r+1]
                    min_len = r-l+1
                if s[l] in t and  window_freq[s[l]] == t_freq[s[l]]:
                    have-=1
                window_freq[s[l]]-=1
                l+=1

        return result

