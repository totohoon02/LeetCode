class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x for x in s.lower() if x.isalnum()]
        return s == s[::-1]