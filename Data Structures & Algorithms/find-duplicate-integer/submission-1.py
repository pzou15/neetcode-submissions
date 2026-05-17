class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # this is so clever and so stupid
        # there is ALWAYS a cycle somewhere if we use elements as pointers to next index
        # head of cycle is the duplicate
        slow = 0
        fast = 0
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]
        return slow