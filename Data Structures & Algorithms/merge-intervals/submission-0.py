class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
# 1,4. 1,9
        for start, end in intervals:
            if stack and stack[-1][1]>=start:
                start = min(stack[-1][0],start)
                end = max(stack[-1][1],end)
                stack[-1] = [start,end]
            else:
                stack.append([start,end])
        
        return stack