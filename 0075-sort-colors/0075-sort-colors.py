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

    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]