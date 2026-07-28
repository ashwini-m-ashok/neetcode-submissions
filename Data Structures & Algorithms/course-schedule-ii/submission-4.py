class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj=defaultdict(list)

        for course, pre_req in prerequisites:
            adj[pre_req].append(course)
            indegree[course]+=1
        
        dq = deque()
        output=[]

        for course in range(numCourses):
            if indegree[course]==0:
                dq.append(course)
        
        while dq:
            pre_req = dq.popleft()
            output.append(pre_req)

            for course in adj[pre_req]:
                indegree[course]-=1
                if indegree[course]==0:
                    dq.append(course)
        
        return output if len(output)==numCourses else []
