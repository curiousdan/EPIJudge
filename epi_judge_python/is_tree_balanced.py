from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# difference in height of its left and right subtree is at most one. 
# given root, return if balanced or not

# HAHA this is the book solution and it also stack overflows loll
#1/6/2021
import collections
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
	StatusHeight = collections.namedtuple("StatusHeight", ("status", "h"))
	def check_balanced(tree):
		if not tree:
			return StatusHeight(True,-1)
		l = check_balanced(tree.left)
		if not l.status:
			return StatusHeight(False, 0)
			
		r = check_balanced(tree.right)
		if not r.status:
			return StatusHeight(False, 0)
		
		status = abs(l.h - r.h) <= 1
		h = max(l.h, r.h)
		return StatusHeight(status, h+1)
	return check_balanced(tree).status
	
# my solution is valid, but gets stack overflow :/
def my_is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
	return False if is_balanced(tree) <=0 else True
	
def my_is_balanced(root):
	if not root:
		return 0
	l = is_balanced(root.left)
	if l < 0:
		return -1
	
	r = is_balanced(root.right)
	if r < 0:
		return -1
		
	if abs(l-r) > 1:
		return -1
	return max(l,r) + 1

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('is_tree_balanced.py', 'is_tree_balanced.tsv',
																																	is_balanced_binary_tree))

