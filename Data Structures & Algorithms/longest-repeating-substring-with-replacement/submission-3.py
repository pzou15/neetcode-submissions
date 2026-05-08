class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # cleaner

        miss = k
        curLen = 0
        maxLen = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    if miss > 0:
                        miss -= 1
                    else:
                        break
                curLen += 1
            if miss > 0:
                curLen = curLen + miss if curLen + miss < len(s) else len(s)
            maxLen = max(maxLen, curLen)
            miss = k
            curLen = 0
        return maxLen
