class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nums = nums[:]
        n = len(nums)
        ops = 0
        
        while n > 1:
            # Check if already non-decreasing
            non_dec = True
            for i in range(1, n):
                if nums[i] < nums[i - 1]:
                    non_dec = False
                    break
            if non_dec:
                return ops
            
            # Find leftmost min sum adjacent pair
            min_sum = float('inf')
            min_idx = -1
            for i in range(n - 1):
                cur_sum = nums[i] + nums[i + 1]
                if cur_sum < min_sum or (cur_sum == min_sum and i < min_idx):
                    min_sum = cur_sum
                    min_idx = i
            
            # Merge
            nums[min_idx] = nums[min_idx] + nums[min_idx + 1]
            del nums[min_idx + 1]
            n -= 1
            ops += 1
        
        return ops
