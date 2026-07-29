class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        visited=set()

        for to, fro in edges:
            adj[to].append(fro)
            adj[fro].append(to)

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei,node)

        count=0
        for node in range(n):
            if node not in visited:
                dfs(node,-1)
                count+=1
        
        return count