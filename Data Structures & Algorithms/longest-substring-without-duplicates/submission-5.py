class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        l=0
        r=0
        window = set()

        for r in range(n):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            max_len = max(max_len, len(window))
            
        
        return max_len
