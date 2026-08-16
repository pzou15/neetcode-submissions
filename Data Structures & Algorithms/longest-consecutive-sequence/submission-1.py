class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsdict = defaultdict(int) # num: length
        max_len = 0

        for n in nums:
            if not numsdict[n]:
                numsdict[n] = numsdict[n-1] + numsdict[n+1] + 1
                numsdict[n - numsdict[n-1]] = numsdict[n]
                numsdict[n + numsdict[n+1]] = numsdict[n]

                max_len = max(numsdict[n], max_len)
        
        
        return max_len

