class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # sliding window:
        # has to be strictly alternating means that the only way window becomes invalid is if 2 in a row is not alternating. meaning r-2 -> r-1 and r-1 -> r are not alternating
        # it only breaks in 2 ways. either it breaks because arr[r-1] and arr[r] are equal or they are the opposite of the expected
        # if they are equal then just move l to r
        # if they are the opposite of expected that means that you can start at r-1 and resume looking for alternate sequencing (l = r-1)
        
        maxLen = 1
        l = 0
        toggle = None
        for r in range(1, len(arr)):
            if toggle == None:
                toggle = arr[r] > arr[r-1]
            if arr[r] == arr[r-1]:
                l = r
                toggle = None
                continue
            if toggle != (arr[r] > arr[r-1]):
                l = r - 1
                toggle = arr[r] > arr[r-1]

            toggle = not toggle
            maxLen = max(maxLen, r - l + 1)


        return maxLen
                