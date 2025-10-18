class Solution:
    def maxDistinctElements(self, nums, k):
        if k == 0:
            return len(set(nums))
        intervals = []
        for x in nums:
            intervals.append((x - k, x + k))
        intervals.sort(key=lambda x: x[1])
        cur = -10**30
        ans = 0
        for L, R in intervals:
            cand = max(L, cur + 1)
            if cand <= R:
                ans += 1
                cur = cand
        return ans
