class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        solution=[]

        def is_palidrome(st):
            l=0
            r=len(st)-1

            while l<=r:
                if st[l]!=st[r]:
                    return False
                l+=1
                r-=1
            return True

        def backtrack(start):
            if start>= len(s):
                res.append(solution.copy())
                return
            
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if is_palidrome(sub):
                    solution.append(sub)
                    backtrack(end+1)
                    solution.pop()
        
        backtrack(0)
        return res
