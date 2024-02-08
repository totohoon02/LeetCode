class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-num for num in nums]
    
        heapq.heapify(h)
        ans = 0

        for i in range(k):
            ans = -heapq.heappop(h)

        return ans