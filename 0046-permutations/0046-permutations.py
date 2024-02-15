class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
      
        def dfs(nums:list, node:list):
                if not nums:
                    res.append(node)

                for i in range(len(nums)):
                    dfs(nums[:i] + nums[i+1:], node + [nums[i]])

        dfs(nums, [])

        return res	