class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = len(nums) * [1]
        prod = 1

        # prefix
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            ret[i] = prod
        # suffix
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i+1]
            ret[i] *= prod
        return ret


        
            
            