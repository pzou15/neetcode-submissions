class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum += n
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
            
        return maxSum