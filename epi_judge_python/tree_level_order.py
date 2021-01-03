from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 8.6
# each node's distance from root is its depth.
# given binary tree, return array consisting of keys at the same level.
# keys sould appear in order of nodes' depths. break ties left to right.


# book solution
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
	result = []
	if not tree:
		return result

	curr_depth_nodes = [tree]

	while curr_depth_nodes:
		# this step just appends the "next level". 
		result.append([curr.data for curr in curr_depth_nodes])

		# okay what the fuck
		curr_depth_nodes = [
			child for curr in curr_depth_nodes for child in (curr.left, curr.right)
			if child
		]

# above code is equivalent to:
#		new = []
#		for curr in curr_depth_nodes:
#			for child in (curr.left, curr.right):
#				if child:
#					new.append(child)
#		curr_depth_nodes = new.copy()

	return result

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('tree_level_order.py', 'tree_level_order.tsv',
																																	binary_tree_depth_order))

