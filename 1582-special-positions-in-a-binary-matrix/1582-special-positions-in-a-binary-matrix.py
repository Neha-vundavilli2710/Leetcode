class Solution:
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        
        row_count = [0] * m
        col_count = [0] * n
        
        # Count number of 1s in each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Check special positions
        special = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1
        
        return special