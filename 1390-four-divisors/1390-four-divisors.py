class Solution:
    def sumFourDivisors(self, nums):
        def sum_if_four_divisors(x):
            divs = set()
            i = 1
            while i * i <= x:
                if x % i == 0:
                    divs.add(i)
                    divs.add(x // i)
                    if len(divs) > 4:
                        return 0
                i += 1
            return sum(divs) if len(divs) == 4 else 0

        total = 0
        for num in nums:
            total += sum_if_four_divisors(num)
        return total
