class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCount = 0
        ret = []

        # zeroes throw prod calculations
        for n in nums:
            print(n)
            if n == 0:
                zeroCount += 1
                # if more than 1 zero then entire array is 0s
                if zeroCount > 1:
                    return len(nums) * [0]
            else:
                prod *= n

        for n in nums:
            if zeroCount > 0:
                if n == 0:
                    ret.append(prod)
                else:
                    ret.append(0)
            else:
                ret.append(prod//n)
        return ret
            
            