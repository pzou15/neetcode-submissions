from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict()
        maxLen = 0
        curLen = 0
        left = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            curLen = right - left + 1
            maxLen = max(curLen, maxLen)

        return maxLen