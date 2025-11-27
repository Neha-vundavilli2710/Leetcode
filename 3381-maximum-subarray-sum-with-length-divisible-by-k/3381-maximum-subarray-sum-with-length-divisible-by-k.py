class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        INF = 10**30
        pref = 0
        min_pref = [INF] * k
        min_pref[0] = 0
        ans = -INF

        for i, x in enumerate(nums, start=1):
            pref += x
            r = i % k
            ans = max(ans, pref - min_pref[r])
            if pref < min_pref[r]:
                min_pref[r] = pref

        return ans
