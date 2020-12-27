from test_framework import generic_test

# can use <<, >>, |, &, ~, ^
# can use equality checks and boolean combinations
def multiply(x: int, y: int) -> int:
		def prim_add(a,b):
			while b:
				carry = a & b
				a = a ^ b
				b = carry << 1
			return a
			
		ret = 0
		while x:
			if x & 1:
				ret = prim_add(ret, y)
			y <<= 1
			x >>= 1
		return ret



# insight is that for eg. 1234 * 4 = 4*4 + 4*3*10 + 4*2*100 + 4*1*1000
# but in binary, its x + 2^k * y, where 2^k * y = y << k

# you must also implement a primitive add 
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
