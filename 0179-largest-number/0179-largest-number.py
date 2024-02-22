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

    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"

        def concat_to_int(a, b):
            return int(str(a) + str(b))

        for i in range(len(nums)):
            for j in range(len(nums)):
                a = concat_to_int(nums[i], nums[j])
                b = concat_to_int(nums[j], nums[i])
                if a > b:
                    nums[i], nums[j] = nums[j], nums[i]
        return "".join(list(map(str, nums)))