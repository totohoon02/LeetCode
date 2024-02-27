class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 카데인 알고리즘
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            # 현재 합과 현재 숫자를 비교 -> 합이 더 크면 현재 숫자가 더해진 것과 같음.
            cur_sum = max(nums[i], cur_sum + nums[i])

            # 값이 맥스인 시점 저장
            max_sum = max(cur_sum, max_sum)
        return max_sum