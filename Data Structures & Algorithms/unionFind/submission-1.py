class UnionFind:
    
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.depths = [0] * n
        self.numComponents = n

    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
    
        if self.depths[root_x] > self.depths[root_y]:
            self.parents[root_y] = root_x
        elif self.depths[root_x] < self.depths[root_y]:
            self.parents[root_x] = root_y
        else:
            self.parents[root_y] = root_x
            self.depths[root_x] += 1
        self.numComponents -= 1
        return True
            
    def getNumComponents(self) -> int:
        return self.numComponents
