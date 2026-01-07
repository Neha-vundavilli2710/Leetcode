class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.ans = 0

        def total(node):
            if not node:
                return 0
            return node.val + total(node.left) + total(node.right)

        total_sum = total(root)

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.ans = max(self.ans, s * (total_sum - s))
            return s

        dfs(root)
        return self.ans % MOD
