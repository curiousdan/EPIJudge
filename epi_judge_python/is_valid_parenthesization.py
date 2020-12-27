from test_framework import generic_test

# Given string "(,),[,]" etc
# see if parenthesis in correct order & correct pairing.
# ({)} is incorrect.

# 12/26/20
def is_well_formed(s: str) -> bool:
	matching_dict = {"}":"{", ")":"(", "]":"["}
	stack = []

	for c in s:
		if not stack or c not in matching_dict:
			stack.append(c)
			continue
		if matching_dict[c] == stack[-1]:
			stack.pop()
		else:
			return False
		
	return True if not stack else False

def booksoln(s):
	stack = []
	lookup = {"(":")", "{":"}", "[":"]"}
	for c in s:
		if c in lookup:
			stack.append(c)
		elif not stack or lookup[stack.pop()] != c: # clever, because the pop step is part of verification
			return False
	return not stack
		
if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('is_valid_parenthesization.py',
																																	'is_valid_parenthesization.tsv',
																																	is_well_formed))

