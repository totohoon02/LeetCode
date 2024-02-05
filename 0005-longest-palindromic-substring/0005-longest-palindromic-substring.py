class Solution:
    def longestPalindrome(self, s: str) -> str:
        curLength = 1
        curStr = ""
        
        #전체가 같을 경우
        if s == s[::-1]: return s

        for i in range(len(s)):
            for j in range(len(s), i, -1):

                if j - i < curLength:
                    break
                
                if s[i:j] == s[i:j][::-1]:
                    curLength = j - i
                    curStr = s[i:j]
        
        return curStr
        

