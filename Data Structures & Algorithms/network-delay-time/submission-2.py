class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        visited=set()
        costs=[math.inf]*(n+1)
        costs[k] = 0
        minheap=[]
        minheap.append((0,k))
        heapq.heapify(minheap)
        total_time = 0

        for src, dest, time in times:
            adj[src].append((dest, time))

        while minheap and len(visited)<n:
            time, to_node = heapq.heappop(minheap)

            if to_node in visited:
                continue
            
            visited.add(to_node)
            
            for nei, cost in adj[to_node]:
                if time+cost<costs[nei]:
                    costs[nei] = time+cost
                    heapq.heappush(minheap,(time+cost, nei))
        total_time = max(costs[1:])
        return total_time if total_time!= math.inf else -1


        
