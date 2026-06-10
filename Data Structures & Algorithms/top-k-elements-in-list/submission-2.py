class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)

        for num in nums:
            num_to_freq[num]+=1
        
        frequency_table = [[] for i in range(len(nums)+1)]
        for num, freq in num_to_freq.items():
            frequency_table[freq].append(num)
        
        output = []
        count=0
        for i in range(len(nums),-1,-1):
            if len(output)==k:
                break
            else:
                for num in frequency_table[i]:
                    output.append(num)
        
        return output