class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        minArr = []
        for i in range(len(nums)):
            #if even
            if i % 2 == 1:
                minArr.append(nums[i])
        
        return sum(minArr)
