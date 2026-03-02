class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        trailing_zeros = []

        # Count trailing zeros for each row
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0

        for i in range(n):
            required = n - i - 1
            j = i
            # Find a row with enough trailing zeros
            while j < n and trailing_zeros[j] < required:
                j += 1
            
            if j == n:  # no row found
                return -1
            
            # Bring row j up to position i
            while j > i:
                trailing_zeros[j], trailing_zeros[j-1] = trailing_zeros[j-1], trailing_zeros[j]
                swaps += 1
                j -= 1

        return swaps