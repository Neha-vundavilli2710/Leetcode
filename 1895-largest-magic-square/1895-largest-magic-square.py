class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*(n+1) for _ in range(m)]
        diag1 = [[0]*(n+1) for _ in range(m)]
        diag2 = [[0]*(n+1) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i][j+1] = (col[i-1][j+1] if i > 0 else 0) + grid[i][j]
                diag1[i][j+1] = (diag1[i-1][j] if i > 0 and j > 0 else 0) + grid[i][j]
                diag2[i][j] = (diag2[i-1][j+1] if i > 0 and j+1 < n else 0) + grid[i][j]

        def check(x, y, k):
            s = row[x][y+k] - row[x][y]
            for i in range(k):
                if row[x+i][y+k] - row[x+i][y] != s:
                    return False
                if col[x+k-1][y+i+1] - (col[x-1][y+i+1] if x > 0 else 0) != s:
                    return False
            if diag1[x+k-1][y+k] - (diag1[x-1][y] if x > 0 else 0) != s:
                return False
            if diag2[x+k-1][y] - (diag2[x-1][y+k] if x > 0 else 0) != s:
                return False
            return True

        ans = 1
        for k in range(2, min(m, n)+1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if check(i, j, k):
                        ans = k
        return ans
