class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for str in strs:
            # sorted("bcd") -> ['b', 'c', 'd']
            sorted_str = "".join(sorted(str))

            # if key exist
            if sorted_str in dic:
                dic[sorted_str].append(str)

            # else
            else:
                dic[sorted_str] = [str]

        return list(dic.values())
