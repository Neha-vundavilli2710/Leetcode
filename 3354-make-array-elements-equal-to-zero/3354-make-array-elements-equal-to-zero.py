class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        valid = 0

        def simulate(start, direction):
            arr = nums[:]
            curr = start
            dir_val = 1 if direction == "right" else -1

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir_val
                else:
                    arr[curr] -= 1
                    dir_val *= -1
                    curr += dir_val
            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if simulate(i, "left"):
                    valid += 1
                if simulate(i, "right"):
                    valid += 1
        return valid
