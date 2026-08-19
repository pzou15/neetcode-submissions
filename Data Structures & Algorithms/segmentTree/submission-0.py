class SegmentTree:
    class Node:
        def __init__(self, sum, L, R):
            self.sum = sum
            self.left = None
            self.right = None
            self.L = L
            self.R = R

           
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, arr, L, R):
        if L == R:
            return self.Node(arr[L], L, R)
        
        M = (L + R) // 2
        root = self.Node(0, L, R)
        root.left = self.build(arr, L, M)
        root.right = self.build(arr, M+1, R)
        root.sum = root.left.sum + root.right.sum

        return root

    
    def update(self, index: int, val: int) -> None:
        return self.update_recurse(self.root, index, val)
    
    def update_recurse(self, root, index, val):
        if root.L == root.R:
            root.sum = val
            return
        
        M = (root.L + root.R) // 2
        if index > M:
            self.update_recurse(root.right, index, val)
        elif index <= M:
            self.update_recurse(root.left, index, val)
        
        root.sum = root.left.sum + root.right.sum
        

    
    def query(self, L: int, R: int) -> int:
        return self.query_recurse(self.root, L, R)
    
    def query_recurse(self, root, L, R):
        if L == root.L and R == root.R:
            return root.sum
        
        M = (root.L + root.R) // 2

        if L > M:
            return self.query_recurse(root.right, L, R)
        elif R <= M:
            return self.query_recurse(root.left, L, R)
        else:
            return self.query_recurse(root.left, L, M) + self.query_recurse(root.right, M+1, R)



