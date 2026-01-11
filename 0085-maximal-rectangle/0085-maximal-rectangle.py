class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = []
            for i in range(cols + 1):
                cur = heights[i] if i < cols else 0
                while stack and cur < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
