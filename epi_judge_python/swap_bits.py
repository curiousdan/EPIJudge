from test_framework import generic_test

# 12/19/20
def swap_bits(x, i, j):
    # x is the number
    # i and j are index locations (from lowest bit)
    if (x >> i) & 1 != (x >> j) & 1:
    	i_bit = 1 << i 
    	j_bit = 1 << j
    	x ^= i_bit | j_bit
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
