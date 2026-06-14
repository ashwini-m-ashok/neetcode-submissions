class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l=0
        r=n-1

        while l<=r and r>=0 and l<n:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        
        return True