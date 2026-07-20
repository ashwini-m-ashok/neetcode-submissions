class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
    
    def search_word(self,node, index , word)-> bool:
        for i in range(index, len(word)):
            c=word[i]
            if c == '.':
                for child in node.children.values():
                    if self.search_word(child, i+1, word):
                        return True
                return False
            elif c in node.children:
                node = node.children[c]
            else:
                return False
        return node.is_word

    def search(self, word: str) -> bool:
        node = self.root
        return self.search_word(node, 0, word)

        
