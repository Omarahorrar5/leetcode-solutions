class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c.lower() for c in s if c.isalnum())
        n = len(clean)
        left, right = 0, n-1
        while left < right:
            if clean[left] != clean[right]:
                return False
            left+=1
            right-=1
        return True