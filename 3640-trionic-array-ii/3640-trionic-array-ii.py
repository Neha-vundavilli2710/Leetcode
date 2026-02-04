from typing import List
import sys

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        INF = sys.maxsize * -1 // 2  # Avoid overflow issues
        inc_ge2 = [INF] * n
        dec_sum = [INF] * n
        inc2_ge2 = [INF] * n
        ans = INF
        
        for i in range(n):
            # First strictly increasing >=2 ending at i
            if i >= 1 and nums[i - 1] < nums[i]:
                # Start new inc len=2
                inc_ge2[i] = nums[i - 1] + nums[i]
                # Extend previous inc_ge2
                if inc_ge2[i - 1] != INF:
                    inc_ge2[i] = max(inc_ge2[i], inc_ge2[i - 1] + nums[i])
            
            # Dec phase after inc_ge2, >=2 dec elems
            if i >= 1:
                # Start new dec len=2 from inc_ge2
                if inc_ge2[i - 1] != INF and nums[i - 1] > nums[i]:
                    dec_sum[i] = inc_ge2[i - 1] + nums[i]
                # Extend dec
                if i >= 2 and nums[i - 1] > nums[i] and dec_sum[i - 1] != INF:
                    if dec_sum[i] == INF:
                        dec_sum[i] = dec_sum[i - 1] + nums[i]
                    else:
                        dec_sum[i] = max(dec_sum[i], dec_sum[i - 1] + nums[i])
            
            # Second inc >=2 after dec
            if i >= 1:
                # Start new inc2 len=2 from dec
                if dec_sum[i - 1] != INF and nums[i - 1] < nums[i]:
                    inc2_ge2[i] = dec_sum[i - 1] + nums[i]
                # Extend inc2
                if i >= 2 and nums[i - 1] < nums[i] and inc2_ge2[i - 1] != INF:
                    if inc2_ge2[i] == INF:
                        inc2_ge2[i] = inc2_ge2[i - 1] + nums[i]
                    else:
                        inc2_ge2[i] = max(inc2_ge2[i], inc2_ge2[i - 1] + nums[i])
            
            if inc2_ge2[i] != INF:
                ans = max(ans, inc2_ge2[i])
        
        return ans
