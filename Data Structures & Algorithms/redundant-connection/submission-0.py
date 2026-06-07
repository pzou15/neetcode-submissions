class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        ranks = [0] * (len(edges)+1)

        for edge in edges:
            if not self.union(edge[0], edge[1], parents, ranks):
                return edge

    
    def find(self, x, parents):
        if x != parents[x]:
            parents[x] = self.find(parents[x], parents)
        
        return parents[x]
    
    def union(self, x, y, parents, ranks):
        parent_x = self.find(x, parents)
        parent_y = self.find(y, parents)

        if parent_x == parent_y:
            return False
        
        if ranks[parent_x] > ranks[parent_y]:
            parents[parent_x] = parents[parent_y]
        elif ranks[parent_x] < ranks[parent_y]:
            parents[parent_y] = parents[parent_x]
        else:
            parents[parent_y] = parents[parent_x]
            ranks[parent_y] += 1
        
        return True



    
