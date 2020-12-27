from test_framework import generic_test

# given string. separated by commas. 
# evaluate the rpn expression 
# eg a,b,Q where Q is arithmetic xpression
# +, -, *, /


# 12/22/20
def evaluate(expression: str) -> int:
	l_form = expression.split(',')
	operation_dict = {
		"+": lambda a, b: a + b,
		"-": lambda a, b: a - b,
		"*": lambda a, b: a * b,
		"/": lambda a, b: a // b
	}
	stack = []
	for value in l_form:
		if value in operation_dict:
			b = stack.pop()
			a = stack.pop()
			result = operation_dict[value](a, b)
			stack.append(result)
		else:
			stack.append(int(value))

	return stack.pop()


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
																																	evaluate))

