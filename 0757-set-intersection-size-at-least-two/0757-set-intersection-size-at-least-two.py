class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        ans = 0
        last1 = -10**18
        last2 = -10**18
        for l, r in intervals:
            if l > last2:
                ans += 2
                last1, last2 = r - 1, r
            elif l > last1:
                ans += 1
                last1, last2 = last2, r
        return ans
