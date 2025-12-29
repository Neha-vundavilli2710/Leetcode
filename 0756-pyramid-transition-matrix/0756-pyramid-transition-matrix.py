class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        from collections import defaultdict

        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[a + b].append(c)

        memo = {}

        def dfs(curr):
            if len(curr) == 1:
                return True
            if curr in memo:
                return memo[curr]

            def build_next(i, path):
                if i == len(curr) - 1:
                    return dfs(path)

                pair = curr[i] + curr[i + 1]
                if pair not in mp:
                    return False

                for ch in mp[pair]:
                    if build_next(i + 1, path + ch):
                        return True
                return False

            memo[curr] = build_next(0, "")
            return memo[curr]

        return dfs(bottom)
