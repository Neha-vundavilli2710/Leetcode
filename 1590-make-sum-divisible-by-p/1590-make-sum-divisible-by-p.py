class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0

        pref = 0
        seen = {0: -1}
        best = len(nums)

        for i, x in enumerate(nums):
            pref = (pref + x) % p
            need = (pref - r) % p
            if need in seen:
                best = min(best, i - seen[need])
            seen[pref] = i

        return best if best < len(nums) else -1
