class Solution:
    def numberOfPaths(self, grid, k):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                for r in range(k):
                    cnt = dp[i][j][r]
                    if cnt == 0:
                        continue
                    if i + 1 < m:
                        nr = (r + grid[i+1][j]) % k
                        dp[i+1][j][nr] = (dp[i+1][j][nr] + cnt) % MOD
                    if j + 1 < n:
                        nr = (r + grid[i][j+1]) % k
                        dp[i][j+1][nr] = (dp[i][j+1][nr] + cnt) % MOD

        return dp[m-1][n-1][0]
