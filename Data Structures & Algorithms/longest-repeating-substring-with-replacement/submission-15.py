from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int) # char : count
        maxLen = 0
        l = 0
        maxCount = 0
        # I'm dumb part 2
        # basically the main thing to know is that k = number of characters in a substring that don't match the majority char
        # if number of chars that don't match majority char > k then it's invalid, this problem doens't care about WHICH char or substring
        # so we can probably just keep a count of what the majority is -> if r - l + 1 - majorityCount > k update left

        for r,c in enumerate(s):
            # get majority char
            freqMap[c] += 1
            maxCount = max(maxCount, freqMap[c])
            # update left pointer against majority char
            while r - l + 1 - maxCount > k:
                freqMap[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen

            
                

                
                             
            
            




    



