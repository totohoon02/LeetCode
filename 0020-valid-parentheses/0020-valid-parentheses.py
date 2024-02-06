class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
          
            else:
                if not stack: return False
                bk = stack[-1]
                if bk == "(" and bracket == ")":
                    stack.pop()
                
                elif bk == "[" and bracket == "]":
                    stack.pop()
                
                elif bk == "{" and bracket == "}":
                    stack.pop()
                
                else:
                    return False
        
        if stack:
            return False
        
        return True