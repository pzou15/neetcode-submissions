class Solution:
    def trap(self, height: List[int]) -> int:
        # the containers must basically consist of 2 high walls and a cavity between them where nothing is as high as the lowest wall.
        # to determine the walls we would go from the outside in -> ends of array do not count as walls
        l = 0
        r = len(height) - 1
        area = 0
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                area += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                area += rightMax - height[r]
        
        return area
            
        

