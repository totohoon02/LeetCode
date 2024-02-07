class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lp = ""
    
        strs.sort(key= lambda x : len(x))
        
        for i, c in enumerate(strs[0]):
            for word in strs[1:]:
                if(word[i] != c): return lp
            lp += c

        return lp