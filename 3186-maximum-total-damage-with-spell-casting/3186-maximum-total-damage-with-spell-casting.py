from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        count = Counter(power)
        unique = sorted(count.keys())
        n = len(unique)
        dp = [0] * n

        for i in range(n):
            curr_val = unique[i]
            curr_damage = curr_val * count[curr_val]

            # find last index j where unique[j] < curr_val - 2
            j = i - 1
            while j >= 0 and unique[j] >= curr_val - 2:
                j -= 1

            if i == 0:
                dp[i] = curr_damage
            else:
                skip = dp[i - 1]
                take = curr_damage + (dp[j] if j >= 0 else 0)
                dp[i] = max(skip, take)

        return dp[-1]
