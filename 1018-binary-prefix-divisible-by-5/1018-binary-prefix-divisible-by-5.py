class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []
        val = 0
        for b in nums:
            val = ((val << 1) + b) % 5
            ans.append(val == 0)
        return ans
