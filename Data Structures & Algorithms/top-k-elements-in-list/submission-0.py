class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, f in freq.items():
            buckets[f].append(n)
        
        res = []
        for i in range(len(buckets) - 1, 0 , -1):
            res.extend(buckets[i])
            if len(res) >= k:
                return res[:k]