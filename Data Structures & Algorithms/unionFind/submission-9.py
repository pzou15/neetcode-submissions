class UnionFind:
    
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x]) # flattens parents tree
        
        return self.parents[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
        
    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        
        parent_x = self.find(x)
        parent_y = self.find(y)
        if self.ranks[parent_x] < self.ranks[parent_y]:
            self.parents[parent_x] = parent_y
        elif self.ranks[parent_x] > self.ranks[y]:
            self.parents[parent_y] = parent_x
        else:
            self.parents[parent_x] = parent_y
            self.ranks[parent_y] += 1
        
        return True

    def getNumComponents(self) -> int:
        count = 0
        for i in range(len(self.ranks)):
            if self.parents[i] == i:
                count += 1
        return count
        


