class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force is kind of more of a pain than just doing it with 2 pointers
        l = 0
        r = len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < len(s) - 1:
                l += 1
            while not s[r].isalnum() and r >= 0:
                r -= 1
            if s[l].casefold() == s[r].casefold():
                l += 1
                r -= 1
            else:
                return False
        return True