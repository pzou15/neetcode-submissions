class Solution:
    def trap(self, height: List[int]) -> int:
        # the containers must basically consist of 2 high walls and a cavity between them where nothing is as high as the lowest wall.
        # to determine the walls we would go from the outside in -> ends of array do not count as walls
        l = 0
        r = len(height) - 1
        area = 0
        leftWall = False
        rightWall = False
        leftWallHeight = 0
        rightWallHeight = 0
        highestWall = 0
        while l < r:
            # scan for walls
            if not leftWall:
                if height[l] > 0 and height[l+1] < height[l]:
                    # left wall
                    leftWall = True
                    leftWallHeight = height[l]
                    print(leftWallHeight)
                else:
                    l += 1

            if not rightWall:
                if height[r] > 0 and height[r-1] < height[r]:
                    # right wall
                    rightWall = True
                    rightWallHeight = height[r]
                    print(rightWallHeight)
                else:
                    r -= 1

            # found walls get highest
            if leftWall and rightWall:
                highestWall = max(leftWallHeight, rightWallHeight)

                # start scanning for next wall
                if highestWall == leftWallHeight:
                    # shift right wall left
                    r -= 1
                    if height[r] < rightWallHeight:
                        area += rightWallHeight - height[r]
                        print(f"new area: {area}")
                    else:
                        rightWallHeight = height[r]
                else:
                    # shift left wall right
                    l += 1
                    if height[l] < leftWallHeight:
                        area += leftWallHeight - height[l]
                    else:
                        # hit new left wall
                        leftWallHeight = height[l]
        
        return area
            
        

