class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        nums.sort()
        start = 1

        for n in nums:
            if start == n:
                start += 1

        return start