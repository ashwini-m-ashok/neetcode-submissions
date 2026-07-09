class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = []

        for w in stones:
            heapq.heappush(minheap,-w)
        
        while len(minheap)>=2:
            w1 = -heapq.heappop(minheap)
            w2 = -heapq.heappop(minheap)
            new_w = abs(w1-w2)

            heapq.heappush(minheap,-new_w)
        
        return -minheap[0]