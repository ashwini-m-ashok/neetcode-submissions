class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        window_len = len(s1)
        window_freq = {}
        substring_freq = {}

        for c in s1:
            substring_freq[c] = 1 + substring_freq.get(c, 0)
        
        for i in range(window_len):
            window_freq[s2[i]] =  1+ window_freq.get(s2[i], 0)
        
        if substring_freq == window_freq:
            return True
        
        l=0
        for r in range(window_len, len(s2)):
            window_freq[s2[l]]-=1
            if window_freq[s2[l]]==0:
                del window_freq[s2[l]]

            l+=1

            window_freq[s2[r]]= 1+ window_freq.get(s2[r], 0)

            if substring_freq == window_freq:
                return True
        
        return False





