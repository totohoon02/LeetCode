class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        
        #Save Keys
        for i in range(len(jewels)):
            dict[jewels[i]] = 0

        #Count values
        for i in range(len(stones)):
            if stones[i] in dict:
                dict[stones[i]] += 1
        
        return sum(dict.values())
