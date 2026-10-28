class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        bucket = [[] for count in range(n+1)]

        for key, freq in counter.items():
            bucket[freq].append(key)
        
        result = []

        for i in range(n, -1, -1):
            if len(bucket[i])>0:
                for item in bucket[i]:
                    result.append(item)
                    if len(result)==k:
                        return result
        
        return result