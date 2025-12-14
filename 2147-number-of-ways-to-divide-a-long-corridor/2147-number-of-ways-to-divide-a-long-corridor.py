class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = 0
        ways = 1
        plants_between = 0
        
        for ch in corridor:
            if ch == 'S':
                seats += 1
                # Every time we finish a pair (except the first),
                # multiply the number of choices
                if seats % 2 == 0:
                    ways = (ways * (plants_between + 1)) % MOD
                    plants_between = 0
            else:  # ch == 'P'
                if seats % 2 == 0 and seats > 0:
                    plants_between += 1
        
        # Total seats must be divisible by 2 and at least one section
        if seats == 0 or seats % 2 != 0:
            return 0
        
        return ways
