from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freqMap = defaultdict(int)
        total = 0
        freqMap[0] = 1
        count = 0
        for n in nums:
            total += n
            if total - k in freqMap:
                count += freqMap[total-k]
            freqMap[total] += 1
        return count
