class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                   if not dfs(nei,node):
                    return False
                elif nei in visited and nei!=parent:
                    return False
            return True

        res=[]
        for to, fro in edges:
            adj[to].append(fro)
            adj[fro].append(to)
            visited = set()

            if not dfs(to, -1):
                return [to, fro]
        return [] 
        
        

