class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, numList in enumerate(mat):
            count1 = sum(numList)
            heapq.heappush(heap, (count1, i))

        ans = [heapq.heappop(heap)[1] for _ in range(k)]

        return ans