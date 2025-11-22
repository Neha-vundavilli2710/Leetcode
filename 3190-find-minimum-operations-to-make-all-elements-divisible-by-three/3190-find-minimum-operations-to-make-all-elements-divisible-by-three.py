class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ops = 0
        for x in nums:
            r = x % 3
            if r == 1 or r == 2:
                ops += 1
        return ops
