class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union = UnionFind(n, edges)
        return union.count_components()

        
            
class UnionFind:
    def __init__(self, n, edges):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        for edge in edges:
            self.union(edge[0], edge[1])

    def find_parent(self, n):
            if n != self.parent[n]:
                self.parent[n] = self.find_parent(self.parent[n])
            return self.parent[n]
        
    def union(self, n1, n2):
        p1 = self.find_parent(n1)
        p2 = self.find_parent(n2)

        if p1 == p2: return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True
    
    def count_components(self) -> int:
        count = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                count += 1
    
        return count