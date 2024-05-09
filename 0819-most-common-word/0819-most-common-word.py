import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        
        words = [word for word in re.sub("[\W]", " ", paragraph).lower().split() if word not in banned]
        count = collections.defaultdict(int)
        for word in words:
            count[word] += 1
        return max(count, key=count.get)