class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        solution=[]
        candidates.sort()
        def bt(i, cur_sum):

            if cur_sum==target:
                res.append(solution[:])
                return
            if cur_sum>target or i>= len(candidates):
                return
            
            solution.append(candidates[i])
            bt(i+1, cur_sum+candidates[i])
            solution.pop()
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            bt(i+1, cur_sum)
        
        bt(0,0)
        return res