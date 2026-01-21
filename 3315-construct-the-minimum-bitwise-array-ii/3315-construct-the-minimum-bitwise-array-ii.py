class Solution:
    def minBitwiseArray(self, nums):
        res = []
        for p in nums:
            ans = -1
            for k in range(31):
                a = p - (1 << k)
                if a >= 0 and (a | (a + 1)) == p:
                    if ans == -1 or a < ans:
                        ans = a
            res.append(ans)
        return res
