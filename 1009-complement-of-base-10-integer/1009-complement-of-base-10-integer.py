class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1  # special case
        num_bits = n.bit_length()  # number of bits in n
        mask = (1 << num_bits) - 1
        return n ^ mask