class Solution:
    def bestClosingTime(self, customers: str) -> int:
        totalY = customers.count('Y')
        
        openPenalty = 0
        remainingY = totalY
        
        minPenalty = totalY
        bestHour = 0
        
        for i, c in enumerate(customers):
            if c == 'Y':
                remainingY -= 1
            else:
                openPenalty += 1
            
            penalty = openPenalty + remainingY
            
            if penalty < minPenalty:
                minPenalty = penalty
                bestHour = i + 1
        
        return bestHour
