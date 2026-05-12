class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = len(nums) - 1
        while l <= r:
            if nums[l] == nums[l-1]:
                val = nums.pop(l)
                nums.append(val)
                r -= 1
            else:
                l += 1

        
        return r + 1
            

            
        
