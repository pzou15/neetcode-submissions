class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.found = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWord(word)
        used = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                # this will update used as it goes and returns the word if it finds one
                self.searchBoard(board, used, i, j, self.root)        
        return self.found
        
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() 
            cur = cur.children[c]
        cur.word = word
    
    def searchBoard(self, board, used, row, col, root):
        cur = root
        if board[row][col] not in cur.children:
            return
        used.add((row,col))

        cur = cur.children[board[row][col]]

        # set used, if it's a word return it
        if cur.word is not None:
            self.found.append(cur.word)
            cur.word = None

        # get neighbors for traversal
        neighbors = []
        if row - 1 >= 0 and (row-1,col) not in used:
            neighbors.append((row-1, col))
        if col - 1 >= 0 and (row, col-1) not in used:
            neighbors.append((row, col-1))
        if row + 1 < len(board) and (row+1, col) not in used:
            neighbors.append((row+1, col))
        if col + 1 < len(board[0]) and (row,col+1) not in used:
            neighbors.append((row, col+1))

        # iterate on neighbors if it finds a word
        for neighbor in neighbors:
            if board[neighbor[0]][neighbor[1]] in cur.children:
                self.searchBoard(board, used, neighbor[0], neighbor[1], cur)
        
        if (row,col) in used:
            used.remove((row,col))



class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
