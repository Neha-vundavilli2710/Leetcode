class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        S = sum(nums)
        return S % k
