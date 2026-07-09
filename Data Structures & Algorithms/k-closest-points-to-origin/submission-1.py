class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []
        for x,y in points:
            dist = math.sqrt((x*x)+(y*y))
            heapq.heappush(minheap,(dist,[x,y]))
        
        while len(res)<k and minheap:
            dist, points = heapq.heappop(minheap)
            res.append(points)

        return res


