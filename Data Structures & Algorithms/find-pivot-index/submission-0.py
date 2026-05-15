class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums = [0]
        total = 0
        for n in nums:
            total += n
            prefixSums.append(total)
        leftSum = 0
        rightSum = 0
        for i in range(1, len(prefixSums)):
            leftSum = prefixSums[i-1]
            rightSum = prefixSums[len(prefixSums)-1] - prefixSums[i]
            if leftSum == rightSum:
                return i - 1
        return -1