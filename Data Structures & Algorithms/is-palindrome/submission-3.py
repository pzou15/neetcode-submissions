class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force is kind of more of a pain than just doing it with 2 pointers
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].casefold() == s[r].casefold():
                l += 1
                r -= 1
            else:
                return False
        return True