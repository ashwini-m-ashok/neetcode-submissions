class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for fro, to in edges:
            adj[to].append(fro)
            adj[fro].append(to)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if not dfs(nei, node):
                        return False

                elif nei in visited and nei!=parent:
                    return False
            return True
        
        return dfs(0, -1) and len(visited)==n