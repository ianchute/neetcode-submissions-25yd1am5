class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        inv = [[] for i in range(len(nums) + 1)]
        for n, c in counts.items():
            inv[c].append(n)

        result = []
        for i in range(len(nums), -1, -1):
            result += inv[i]
            if len(result) >= k:
                result = result[:k]
                break
        return result