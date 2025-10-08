import bisect
import math

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        res = []
        
        for s in spells:
            target = math.ceil(success / s)
            idx = bisect.bisect_left(potions, target)
            res.append(m - idx)
        
        return res
