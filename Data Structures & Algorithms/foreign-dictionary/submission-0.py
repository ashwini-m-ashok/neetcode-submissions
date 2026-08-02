class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}

        for w in words:
            for c in w:
                adj[c] = set()

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1),len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ''
            
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break



        cycle = set()
        visited = set()
        res = []

        def dfs(char):
            if char in cycle:
                return False

            if char in visited:
                return True

            cycle.add(char)

            for nei in adj[char]:
                if not dfs(nei):
                    return False

            cycle.remove(char)
            visited.add(char)
            res.append(char)
            return True
        
        for c in adj:
            if not dfs(c):
                return ''
        
        res.reverse()
        return ''.join(res)

