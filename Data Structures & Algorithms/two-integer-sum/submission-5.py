class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        snums = sorted(nums)
        a, b = 0, len(nums) - 1

        while True:
            assert a < b, "no solution"
            curr = snums[a] + snums[b]
            if curr == target:
                break
            elif curr > target:
                b -= 1
            else:
                a += 1

        return sorted([
            nums.index(snums[a]), 
            n - list(reversed(nums)).index(snums[b]) - 1
        ])