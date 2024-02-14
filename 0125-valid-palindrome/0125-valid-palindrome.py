class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ns = re.sub('[^a-z0-9]', '', s)
        
        return ns == ns[::-1]