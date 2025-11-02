class Solution:
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0] * n for _ in range(m)]  # 0: empty, 1: guard, 2: wall, 3: guarded
        
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        # directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in (1, 2):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc

        # Count unguarded cells
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count
