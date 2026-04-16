class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        left = 0
        right = k
        window = set()
        for i in range(min(len(nums),k + 1)):
            if nums[i] not in window:
                window.add(nums[i])
            else:
                return True
        
        for i in range(1, len(nums)-k):
            window.remove(nums[left])
            left = i
            right += 1
            if nums[right] not in window:
                window.add(nums[right])
            else:
                return True
        
        return False