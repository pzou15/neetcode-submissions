class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = width * height
        # since it is a container for water the max area is bound by the lowest "bar"
        # brute force would be to try every possible combination and just get max height
        # however there are a lot of useless calculations in the brute force
        # for one thing we know that to maximize area we should maximize both width and height
        # width is determined by the length of the array so we should try the maximum width first
        # I would use 2 pointers to get the width and we will shift pointers based on maximum height of the next possible pointer
        # this is what I was afraid of. Rather than determine absolute max, let's go with relative max as in largest difference.
        #
        
        l = 0
        r = len(heights)-1
        maxArea = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea

        