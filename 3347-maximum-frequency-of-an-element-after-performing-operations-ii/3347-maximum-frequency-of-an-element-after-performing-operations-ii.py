from collections import Counter, defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        if not nums:
            return 0
        freq = Counter(nums)
        events = defaultdict(int)
        for x in nums:
            l = x - k
            r = x + k
            events[l] += 1
            events[r + 1] -= 1
        positions = sorted(set(events.keys()) | set(freq.keys()))
        cur = 0
        ans = 0
        for pos in positions:
            cur += events.get(pos, 0)
            cover = cur
            cnt_eq = freq.get(pos, 0)
            possible = min(cnt_eq + numOperations, cover)
            ans = max(ans, possible)
            ans = min(ans, len(nums))
        return ans
