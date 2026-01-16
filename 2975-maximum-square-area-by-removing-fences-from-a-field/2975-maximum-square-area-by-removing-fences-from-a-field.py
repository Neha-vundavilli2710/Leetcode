class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        h = [1] + hFences + [m]
        v = [1] + vFences + [n]

        h.sort()
        v.sort()

        hs = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                hs.add(h[j] - h[i])

        ans = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in hs:
                    ans = max(ans, d)

        if ans == 0:
            return -1
        return (ans * ans) % MOD
