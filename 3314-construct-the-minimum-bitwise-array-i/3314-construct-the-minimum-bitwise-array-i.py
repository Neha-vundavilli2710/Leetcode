class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
                continue
            res = -1
            for a in range(x):
                if (a | (a + 1)) == x:
                    res = a
                    break
            ans.append(res)
        return ans
