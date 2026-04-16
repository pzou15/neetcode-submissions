class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        total = 0
        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            maxSum = max(curMax, maxSum)
            minSum = min(curMin, minSum)
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum

        