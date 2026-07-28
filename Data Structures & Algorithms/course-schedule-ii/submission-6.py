class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj=defaultdict(list)

        for course, pre_req in prerequisites:
            adj[course].append(pre_req)
        
        output=[]
        cycle=set()
        visited=set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            
            for crs in adj[course]:
                if not dfs(crs):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output
