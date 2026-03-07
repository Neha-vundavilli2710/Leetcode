class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s  # simulate rotations
        pattern1 = ['0', '1'] * n  # 010101...
        pattern2 = ['1', '0'] * n  # 101010...
        
        min_flips = float('inf')
        flips1 = flips2 = 0
        left = 0
        
        for right in range(2*n):
            if t[right] != pattern1[right]:
                flips1 += 1
            if t[right] != pattern2[right]:
                flips2 += 1
            
            # When window size exceeds n, slide left
            if right - left + 1 > n:
                if t[left] != pattern1[left]:
                    flips1 -= 1
                if t[left] != pattern2[left]:
                    flips2 -= 1
                left += 1
            
            # When window size == n, check minimum
            if right - left + 1 == n:
                min_flips = min(min_flips, flips1, flips2)
        
        return min_flips