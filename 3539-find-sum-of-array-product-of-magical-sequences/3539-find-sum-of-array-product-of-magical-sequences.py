from itertools import combinations

class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        ans = 0
        # iterate over all choices of k distinct indices
        for subset in combinations(range(n), k):
            vals = [nums[i] for i in subset]

            # inclusion-exclusion over subsets T of S:
            # contribution = sum_{T subset S} (-1)^{k-|T|} (sum_{i in T} vals[i])^m
            total = 0
            # t = size of T
            for t in range(0, k+1):
                sign = -1 if (k - t) % 2 == 1 else 1
                # iterate all subsets of size t
                for sub in combinations(vals, t):
                    ssum = sum(sub) % MOD
                    # 0^m = 0 when m>=1, so empty subset contributes 0; pow handles it
                    total = (total + sign * pow(ssum, m, MOD)) % MOD

            ans = (ans + total) % MOD

        return ans % MOD
