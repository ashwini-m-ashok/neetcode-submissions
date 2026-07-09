class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []

        for num in nums:
            heapq.heappush(maxheap, num)
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        
        return maxheap[0]
