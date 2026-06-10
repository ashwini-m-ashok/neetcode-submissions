class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s))+'#'+s
        return result

    def decode(self, s: str) -> List[str]:
        i=0
        output = []

        while i<len(s):
            cur_len = 0
            idx = i
            while idx<len(s) and s[idx]!='#':
                cur_len = cur_len*10+ int(s[idx])
                idx+=1
            i=idx+1
            output.append(s[i:i+cur_len])
            i+=cur_len
        
        return output
