class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero = False
        
        for char in s:
            if char == '0':
                seen_zero = True
            elif char == '1' and seen_zero:
                # Second segment of ones
                return False
        
        return True