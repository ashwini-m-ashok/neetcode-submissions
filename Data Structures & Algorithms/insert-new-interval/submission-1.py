class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack=[]
        i=0
        while i<len(intervals):
            start=intervals[i][0]
            end = intervals[i][-1]
            if end>=newInterval[0]:
                break
            stack.append([start,end])
            i+=1

        new_start=newInterval[0]
        new_end = newInterval[1]

        while i<len(intervals) and intervals[i][0]<=new_end:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1],new_end)
            i+=1
        
        stack.append([new_start,new_end])

        while i<len(intervals):
            start=intervals[i][0]
            end = intervals[i][-1]
            stack.append([start,end])
            i+=1
        
        return stack
            
