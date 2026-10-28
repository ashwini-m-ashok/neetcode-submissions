class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []

        for key, freq in counter.items():
            heapq.heappush(res, (freq, key))
            if len(res) > k:
                heapq.heappop(res)
        
        result = []

        for f, val in res:
            result.append(val)
        
        return result