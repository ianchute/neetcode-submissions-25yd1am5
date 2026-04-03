class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        seen = set()
        for n in nums:
            if n in seen:
                result = True
                break
            else:
                seen.add(n)
        return result