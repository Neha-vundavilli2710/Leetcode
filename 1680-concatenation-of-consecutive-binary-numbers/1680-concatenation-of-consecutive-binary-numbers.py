class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0
        bits = 0
        
        for i in range(1, n+1):
            
            # Increase bit length at powers of 2
            if i & (i-1) == 0:
                bits += 1
            
            res = ((res << bits) | i) % MOD
        
        return res