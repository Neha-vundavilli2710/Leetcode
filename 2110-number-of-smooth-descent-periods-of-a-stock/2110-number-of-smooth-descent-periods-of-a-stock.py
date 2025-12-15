class Solution:
    def getDescentPeriods(self, prices):
        n = len(prices)
        ans = 0
        length = 1  # current descent length
        
        for i in range(n):
            if i > 0 and prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                length = 1
            ans += length
        
        return ans
