from test_framework import generic_test

# Parity of word is 1 if number of ones is odd
# it is 0 if even.

# PASSED Dec 19 2020
def parity(x: int) -> int:
    ret = 0
    while x:
    	base_bit = x&1
    	ret ^= base_bit
    	x >>= 1
    return ret
    
    
def book_soln1(x: int ) -> int:
	ret = 0
	while x:
		ret ^= 1
		x &= x - 1 # drops the lowest set bit of x
	return ret
	
def book2 (x):
	# this only works for numbers that are exactly 64 bits
	# 
	x ^= x >> 32
	x ^= x >> 16
	x ^= x >> 8
	x ^= x >> 4
	x ^= x >> 2
	x ^= x >> 1
	return x&1
	


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
