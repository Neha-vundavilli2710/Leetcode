class Solution:
    def minOperations(self, s: str) -> int:
        count0, count1 = 0, 0
        
        for i, c in enumerate(s):
            # Expected char if pattern starts with '0'
            if c != str(i % 2):
                count0 += 1
            # Expected char if pattern starts with '1'
            if c != str((i + 1) % 2):
                count1 += 1
        
        return min(count0, count1)