class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for char in s:
            if char.isalnum():
                ns += char.lower()
        
        return ns == ns[::-1]