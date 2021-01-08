from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# 9.5
# 1/7/21
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
	# the insight is that bit shift left is eequal to 2*number
	def helper(tree, partial_sum):
		if not tree:
			return 0
		partial_sum = (partial_sum << 1) + tree.data
		
		# necessary, because leaf MUST return the sum at that point
		if not tree.left and not tree.right:
			return partial_sum

		# non-leaves just return the sum of its returned values. 
		l = r= 0
		if tree.left:
			l = helper(tree.left, partial_sum)
		if tree.right:
			r = helper(tree.right, partial_sum)
		return l + r
	return helper(tree, 0)
					
		

# book soln. wow very clever. Actually faster than reimplementation above. 
# seems like if statements take longer than simple recursion.
def book_sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def sum_root_to_leaf_helper(tree, partial_path_sum=0):
        if not tree:
            return 0

        partial_path_sum = partial_path_sum *2 + tree.data
        if not tree.left and not tree.right:  # Leaf.
            return partial_path_sum
        # Non-leaf.
        return (sum_root_to_leaf_helper(tree.left, partial_path_sum) +
                sum_root_to_leaf_helper(tree.right, partial_path_sum))

    return sum_root_to_leaf_helper(tree)

from functools import reduce	
def attempt1_sum_root_to_leaf(tree: BinaryTreeNode) -> int:
	if not tree:
		return 0
		
	def build_paths(node):
		l = r = []
		if node.left:	
			l = build_paths(node.left)
		if node.right:
			r = build_paths(node.right)
		combined = l + r
		if not combined:
			return [str(node.data)]
		return [str(node.data) + element for element in combined]
		
	all_paths = build_paths(tree)
	all_paths[0] = int(all_paths[0],2)
	int_and_sum = lambda x, y: x+int(y,2)
	return reduce(int_and_sum, all_paths)


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('sum_root_to_leaf.py', 'sum_root_to_leaf.tsv',
																																	sum_root_to_leaf))

