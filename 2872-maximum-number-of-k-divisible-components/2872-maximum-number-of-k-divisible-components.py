class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 0
        seen = [False] * n

        def dfs(u):
            nonlocal ans
            seen[u] = True
            total = values[u]

            for v in g[u]:
                if not seen[v]:
                    subtotal = dfs(v)
                    total += subtotal

            if total % k == 0:
                ans += 1
                return 0

            return total

        dfs(0)
        return ans
