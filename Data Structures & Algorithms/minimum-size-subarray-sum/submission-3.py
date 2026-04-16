class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curSum = 0
        minLen = float("inf")
        for right in range(len(nums)):
            if nums[right] >= target:
                return 1
            curSum += nums[right]
            if curSum >= target:
                while (left != right and curSum >= target):
                    minLen = min(minLen, right - left + 1)
                    curSum -= nums[left]
                    left += 1     
            
        
        return minLen if minLen < float("inf") else 0