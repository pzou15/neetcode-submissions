import string
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        depth = len(word)
        for c in word:
            cur.depth = max(cur.depth, depth)
            depth -= 1
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        return self.searchRecurse(word, cur)
        
    def searchRecurse(self, word, root):
        cur = root
        for i in range(len(word)):
            if word[i] == '.':
                for c in string.ascii_lowercase:
                    tail = ""
                    if i + 1 < len(word):
                        tail = word[i+1:]
                    remaining = c + tail
                    if len(remaining) > cur.depth:
                        continue
                    found = self.searchRecurse(remaining, cur)
                    if found:
                        return True
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]
        return cur.word
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.depth = 0