from collections import Counter
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if n < 3:
            return 0

        left = Counter()
        right = Counter(nums)  # counts of elements to the right (including current)

        ans = 0
        for j in range(n):
            val = nums[j]
            # move current out of right (so right now represents k > j)
            right[val] -= 1

            target = val * 2
            # number of i on left with value == 2*val times number of k on right with value == 2*val
            ans = (ans + left[target] * right[target]) % MOD

            # move current into left (so left now represents i < j for future j)
            left[val] += 1

        return ans