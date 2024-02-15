class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        
        
        len_digit = len(digits)
        if len_digit == 0: return []
        result = []
        
        def dfs(idx, s):
            if len(s) == len_digit:
                result.append(s)
                return

            for i in range(idx, len_digit):
                for j in graph[digits[i]]:
                    dfs(i+1, s+j)
        
        dfs(0, "")    
        return result    
    
       