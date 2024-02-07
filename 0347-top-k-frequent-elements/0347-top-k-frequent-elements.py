class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_dict = sorted(counter.items(), key= lambda item: item[1], reverse=True)
        topK = [item[0] for item in sorted_dict][:k]
        return topK   