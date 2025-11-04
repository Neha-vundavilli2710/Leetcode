from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        res = []

        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = Counter(window)
            freq_sorted = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))[:x]

            total = 0
            for val, count in freq_sorted:
                total += val * count
            res.append(total)

        return res
