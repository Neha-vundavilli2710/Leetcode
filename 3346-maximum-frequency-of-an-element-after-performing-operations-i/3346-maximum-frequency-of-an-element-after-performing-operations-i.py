class Solution:
    def maxFrequency(self, nums, k, numOperations):
        if not nums:
            return 0
        from collections import Counter
        freq = Counter(nums)
        minV = min(nums) - k
        maxV = max(nums) + k
        offset = -minV
        size = maxV - minV + 3
        diff = [0] * size
        for v in nums:
            l = v - k + offset
            r = v + k + offset
            if l < 0:
                l = 0
            if r + 1 >= size:
                r = size - 2
            diff[l] += 1
            diff[r + 1] -= 1
        best = 0
        cur = 0
        for idx in range(size - 2):
            cur += diff[idx]
            t = idx - offset
            cnt_equal = freq.get(t, 0)
            cnt_cover = cur
            possible = cnt_equal + min(numOperations, cnt_cover - cnt_equal)
            if possible > best:
                best = possible
        return best
