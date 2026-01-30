from collections import defaultdict

class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        n = len(source)

        rules = defaultdict(dict)
        for o, c, w in zip(original, changed, cost):
            if c not in rules[o] or rules[o][c] > w:
                rules[o][c] = w

        groups = defaultdict(set)
        for o in rules:
            for c in rules[o]:
                groups[len(o)].add(o)
                groups[len(o)].add(c)

        dist = {}

        for L in groups:
            strs = list(groups[L])
            idx = {s: i for i, s in enumerate(strs)}
            m = len(strs)

            d = [[INF]*m for _ in range(m)]
            for i in range(m):
                d[i][i] = 0

            for o in rules:
                if len(o) == L:
                    for c in rules[o]:
                        d[idx[o]][idx[c]] = min(d[idx[o]][idx[c]], rules[o][c])

            for k in range(m):
                for i in range(m):
                    for j in range(m):
                        if d[i][k] + d[k][j] < d[i][j]:
                            d[i][j] = d[i][k] + d[k][j]

            for i in range(m):
                for j in range(m):
                    dist[(strs[i], strs[j])] = d[i][j]

        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue

            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])

            for L in groups:
                if i + L <= n:
                    s = source[i:i+L]
                    t = target[i:i+L]
                    if (s, t) in dist and dist[(s, t)] < INF:
                        dp[i+L] = min(dp[i+L], dp[i] + dist[(s, t)])

        return dp[n] if dp[n] != INF else -1
