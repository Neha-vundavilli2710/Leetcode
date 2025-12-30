class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                if self.isMagic(grid, i, j):
                    count += 1
        return count

    def isMagic(self, grid, r, c):
        nums = set()
        for i in range(3):
            for j in range(3):
                val = grid[r + i][c + j]
                if val < 1 or val > 9:
                    return False
                nums.add(val)

        if len(nums) != 9:
            return False

        # center must be 5
        if grid[r + 1][c + 1] != 5:
            return False

        s = sum(grid[r][c:c+3])

        # rows
        for i in range(3):
            if sum(grid[r + i][c:c+3]) != s:
                return False

        # columns
        for j in range(3):
            if grid[r][c + j] + grid[r + 1][c + j] + grid[r + 2][c + j] != s:
                return False

        # diagonals
        if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != s or
            grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != s):
            return False

        return True
