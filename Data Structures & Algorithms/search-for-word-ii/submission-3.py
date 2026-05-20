class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.found = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWord(word)
        used = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
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
        used[row][col] = 1

        cur = cur.children[board[row][col]]

        # set used, if it's a word return it
        if cur.word is not None:
            self.found.append(cur.word)
            cur.word = None

        # get neighbors for traversal
        neighbors = []
        if row - 1 >= 0 and not used[row-1][col]:
            neighbors.append((row-1, col))
        if col - 1 >= 0 and not used[row][col-1]:
            neighbors.append((row, col-1))
        if row + 1 < len(board) and not used[row+1][col]:
            neighbors.append((row+1, col))
        if col + 1 < len(board[0]) and not used[row][col+1]:
            neighbors.append((row, col+1))

        # iterate on neighbors if it finds a word
        for neighbor in neighbors:
            if board[neighbor[0]][neighbor[1]] in cur.children:
                self.searchBoard(board, used, neighbor[0], neighbor[1], cur)
        
        used[row][col] = 0



class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
