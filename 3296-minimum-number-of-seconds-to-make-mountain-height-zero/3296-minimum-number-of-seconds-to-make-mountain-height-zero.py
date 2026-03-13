import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def canFinish(T):
            total = 0
            for w in workerTimes:
                # Solve x^2 + x - 2*T/w <= 0
                val = int((-1 + math.sqrt(1 + 8*T/w)) // 2)
                total += val
                if total >= mountainHeight:
                    return True
            return False
        
        left, right = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer