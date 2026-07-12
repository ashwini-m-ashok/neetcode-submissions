class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num: int) -> None:
        if not (self.minheap) and not (self.maxheap):
            heapq.heappush(self.maxheap,-num)
        elif self.minheap and num>self.minheap[0]:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush(self.maxheap,-num)
        
        if abs(len(self.minheap)-len(self.maxheap))>1:
            if len(self.maxheap)>len(self.minheap):
                heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
            else:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.minheap)>len(self.maxheap): 
            return self.minheap[0]
        elif len(self.maxheap)>len(self.minheap):
            return -self.maxheap[0]
        else:
            return (self.minheap[0]+-self.maxheap[0])/2
        
        