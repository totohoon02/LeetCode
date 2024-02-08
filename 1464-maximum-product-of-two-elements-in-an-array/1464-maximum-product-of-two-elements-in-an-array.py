import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []

        #heapify
        for num in nums:
            heapq.heappush(heap, -num)

        #ext 2
        num1 = -heapq.heappop(heap)        
        num2 = -heapq.heappop(heap)
        
        ans = (num1 - 1) * (num2 - 1)

        return ans    