class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        chars = [[] for _ in range(numRows)]
        
        dir = 1
        cur = 0
        
        for c in s:
            chars[cur].append(c)
            cur += 1 * dir
            
            if cur == numRows - 1 or cur == 0:
                dir *= -1
        
        chars = ["".join(char) for char in chars]
        return "".join(chars)