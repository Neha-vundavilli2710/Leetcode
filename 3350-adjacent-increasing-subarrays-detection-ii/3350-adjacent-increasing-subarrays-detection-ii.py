class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        L = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                L[i] = L[i + 1] + 1
        def check(k):
            limit = n - 2 * k + 1
            if limit <= 0:
                return False
            for a in range(limit):
                if L[a] >= k and L[a + k] >= k:
                    return True
            return False
        lo, hi, ans = 1, n // 2, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
