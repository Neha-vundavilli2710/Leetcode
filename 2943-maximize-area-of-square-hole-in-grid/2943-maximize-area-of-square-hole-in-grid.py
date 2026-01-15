class Solution:
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def longest_consecutive(arr):
            arr.sort()
            longest = 1
            curr = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                    if curr > longest:
                        longest = curr
                else:
                    curr = 1
            return longest

        max_h = longest_consecutive(hBars) + 1
        max_v = longest_consecutive(vBars) + 1

        side = min(max_h, max_v)
        return side * side
