class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        solution=[]
        candidates.sort()

        def backtrack(index, cur_sum):
            
            if cur_sum == target:
                res.append(solution.copy())
                return
            if index>=len(candidates) or cur_sum > target:
                return
            solution.append(candidates[index])
            backtrack(index+1, candidates[index]+cur_sum)
            solution.pop()

            while index+1<len(candidates) and candidates[index]==candidates[index+1]:
                index+=1
            backtrack(index+1, cur_sum)
        
        backtrack(0,0)
        return res
