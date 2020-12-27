from test_framework import generic_test

#12/20/20

# weight of a nonnegative integer is the number of bits that are
# set to 1 in its binary represeantation. 
# Assume that x is <= 64 bits
def closest_int_same_bit_count(x: int) -> int:
    for i in range(63):
    	if (x>>i) & 1 != (x>>(i+1)) & 1:
    		bit_mask = (1<<i)|(1<<i+1)
    		return x ^ bit_mask
    raise ValueError("wtf bro give me good inputs")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
