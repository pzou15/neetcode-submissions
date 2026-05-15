class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [1]
        leftProd = 1
        for n in nums:
            leftProd *= n
            preProd.append(leftProd)
        postProd = [1] * (len(nums) + 1)
        rightProd = 1
        for i in range(len(nums) - 1, -1, -1):
            rightProd *= nums[i]
            postProd[i] = rightProd
        ret = []
        for i in range(len(nums)):
            left = preProd[i]
            right = postProd[i+1]
            total = left * right
            ret.append(total)
        return ret

        
            
            