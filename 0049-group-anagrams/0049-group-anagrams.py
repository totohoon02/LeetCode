class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            sorted_word = "".join(sorted(list(str)))
            if res.get(sorted_word):
                res[sorted_word].append(str)
            else:
                res[sorted_word] = [str]
        return list(res.values())
