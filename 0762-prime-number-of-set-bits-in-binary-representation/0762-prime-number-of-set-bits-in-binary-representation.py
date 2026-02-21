class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cntPrimeSetBits = 0
        # The mask represents primes: 2, 3, 5, 7, 11, 13, 17, 19
        magicMask = 665772

        for num in range(left, right + 1):
            # num.bit_count() counts set bits in Python 3.8+
            if (magicMask >> num.bit_count()) & 1:
                cntPrimeSetBits += 1

        return cntPrimeSetBits