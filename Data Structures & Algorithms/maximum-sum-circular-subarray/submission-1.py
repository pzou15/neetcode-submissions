class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum = 0
        maxFwdSum = nums[0]
        maxBwdSum = nums[0]
        n = len(nums)
        index = 0
        startIndex = 0
        for i in range(n * 2):
            if curSum < 0:
                curSum = 0
                startIndex = index
            curSum += nums[index]
            maxFwdSum = max(curSum, maxFwdSum)
            index = (index + 1) % n
            if index == startIndex:
                break
        curSum = 0
        for i in range(n * 2):
            if curSum < 0:
                curSum = 0
                startIndex = index
            curSum += nums[index]
            maxBwdSum = max(curSum, maxBwdSum)
            index = (index - 1) % n
            if index == startIndex:
                break
        maxSum = max(maxFwdSum, maxBwdSum)
        return maxSum
            