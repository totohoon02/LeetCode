class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            cur = nums[i]
            diff = target - cur
            if diff in dict:
                return [i, dict[diff]]
            else:
                dict[cur] = i

