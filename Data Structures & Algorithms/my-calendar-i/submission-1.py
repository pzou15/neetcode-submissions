class MyCalendar:
    class Node:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
        

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root is None:
            self.root = self.Node(startTime, endTime)
            return True
        return self.add_booking(self.root, startTime, endTime)
        
    def add_booking(self, root, start, end):
        if end <= root.start:
            if root.left is None:
                root.left = self.Node(start, end)
                return True
            return self.add_booking(root.left, start, end)
        elif start >= root.end:
            if root.right is None:
                root.right = self.Node(start, end)
                return True
            return self.add_booking(root.right, start, end)
        else:
            return False
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)