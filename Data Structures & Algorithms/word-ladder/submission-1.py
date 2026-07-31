class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or len(beginWord)!=len(endWord):
            return 0
        wordList.append(beginWord)
        patterns = collections.defaultdict(list) # stores *ot: hot, dot, lot

        for word in wordList:
            for j in range(len(word)):
                pat = word[:j]+'*'+word[j+1:]
                patterns[pat].append(word)
        
        dq = deque()
        dq.append(beginWord)

        res=1
        visit = set([beginWord])
        while dq:
            for _ in range(len(dq)):
                
                word = dq.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pat = word[:j]+'*'+word[j+1:]
                    
                    for nei in patterns[pat]:
                        if nei not in visit:
                            dq.append(nei)
                            visit.add(nei)
            
            res+=1
        return 0
            

