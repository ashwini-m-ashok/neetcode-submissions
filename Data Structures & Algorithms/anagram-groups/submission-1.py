class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for s in strs:
            hash_table = [0]*26
            i=0
            for i in range(len(s)):
                hash_table[ord(s[i])-ord('a')]+=1
            freq_map[tuple(hash_table)].append(s)
        
        return list(freq_map.values())
