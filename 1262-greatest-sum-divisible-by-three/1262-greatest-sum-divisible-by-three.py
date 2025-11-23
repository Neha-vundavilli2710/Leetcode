class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        s = sum(nums)
        if s % 3 == 0:
            return s

        r1 = []
        r2 = []
        for x in nums:
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)

        r1.sort()
        r2.sort()

        if s % 3 == 1:
            a = r1[0] if r1 else 10**15
            b = r2[0] + r2[1] if len(r2) >= 2 else 10**15
            return s - min(a, b)

        a = r2[0] if r2 else 10**15
        b = r1[0] + r1[1] if len(r1) >= 2 else 10**15
        return s - min(a, b)
