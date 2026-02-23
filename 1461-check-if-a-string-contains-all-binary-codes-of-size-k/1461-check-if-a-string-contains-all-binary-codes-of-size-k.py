class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        
        if n - k + 1 < (1 << k):
            return False
        
        seen = set()
        mask = (1 << k) - 1
        curr = 0
        
        for i in range(n):
            # Shift left and add new bit
            curr = ((curr << 1) & mask) | int(s[i])
            
            # Start recording after first k bits
            if i >= k - 1:
                seen.add(curr)
                
                # Early exit optimization
                if len(seen) == (1 << k):
                    return True
        
        return False