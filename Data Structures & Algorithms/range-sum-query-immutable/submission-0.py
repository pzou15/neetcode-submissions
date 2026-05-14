class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = []
        total = 0
        for n in nums:
            total += n
            self.prefixSums.append(total)
    def sumRange(self, left: int, right: int) -> int:
        total = self.prefixSums[right] - self.prefixSums[left-1] if left - 1 >= 0 else self.prefixSums[right]
        return total
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)