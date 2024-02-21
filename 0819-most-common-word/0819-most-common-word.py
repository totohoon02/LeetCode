import collections

class Solution:
    def __init__(self):
        pass

    def readline(self, as_int=True):
        import sys
        input = sys.stdin.readline
        line = input().split(" ")
        if len(line) == 1:
            return int(line[0])
        if as_int:
            return list(map(int, line))
        else:
            return line

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        words = [word for word in re.sub("[\W]", " ", paragraph).lower().split() if word not in banned]
        count = collections.defaultdict(int)
        for word in words:
            count[word] += 1
        return max(count, key=count.get)