class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            # Flip the i-th character of the i-th string
            ans.append('0' if nums[i][i] == '1' else '1')
        return ''.join(ans)