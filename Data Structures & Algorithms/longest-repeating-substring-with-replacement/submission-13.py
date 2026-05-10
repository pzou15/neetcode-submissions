class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        maxLen = 0
        # I'm dumb
        for c in chars:
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1 # count number of char c in substring
                while (r - l + 1) - count > k: # slide left is use up bridges
                    if s[l] == c:
                        count -= 1
                    l += 1
                maxLen = max(maxLen, r - l + 1)
        
        return maxLen

            
                

                
                             
            
            




    



