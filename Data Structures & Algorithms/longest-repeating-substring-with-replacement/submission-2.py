class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k can act as a replacement to extend the longest substring either left or right
        # k can act as a bridge to connect 2 substrings of the same character
        # need to find max(extended, bridged)
        # brute force option, iterate from each index using the start index as the "repetition char"
        # when out of repetitions attempt to look backwards or forwards k+1 indices. If repetition resumes:
        # continue counting
        # if repetition does not resume verify if there are up to k spaces behind or ahead
        # this is a brute force approach
        miss = k
        curLen = 0
        maxLen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    curLen += 1
                else:
                    if miss > 0:
                        miss -= 1
                        curLen += 1
                    else:
                        break
            if miss > 0:
                curLen = curLen + miss if curLen + miss < len(s) else len(s)
            maxLen = max(maxLen, curLen)
            miss = k
            curLen = 0
        return maxLen