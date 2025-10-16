class Solution:
    def findSmallestInteger(self, nums, value):
        from collections import Counter
        count = Counter([num % value for num in nums])
        res = 0
        while count[res % value]:
            count[res % value] -= 1
            res += 1
        return res
