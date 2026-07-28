class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0]*numCourses

        for course, prereq in prerequisites:
            indegree[course]+=1
            adj[prereq].append(course)
        
        dq = deque()

        for course in range(numCourses):
            if indegree[course]==0:
                dq.append(course)
        
        finished=0
        while dq:
            completed_course = dq.popleft()
            finished+=1
            for course in adj[completed_course]:
                indegree[course]-=1
                if  indegree[course]==0:
                    dq.append(course)
        
        return finished==numCourses
        
        

