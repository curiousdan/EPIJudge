from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Tree is symmetric if you can draw a vertical line thru root and left subtree is mirror of right.
# my solution would have performed an inorder (left root right) traversal of left and right of the root
# and done a full comparison of the two lists at the top. The following book solution is much more elegant and
# lovable. 

# my implementation of book
def my_is_symmetric(tree: BinaryTreeNode) -> bool:
	def traversal(left, right):
		if not left and not right: # both empty
			return True
		elif left and right: # neither empty
			# this is optimized because it avoids right traversal if left is wrong
			if left.data != right.data:
				return False
			if not traversal(left.left, right.right):
				return False
			if not traversal(left.right, right.left):
				return False
			return True
		return False # one empty other not
			
	return not tree or traversal(tree.left, tree.right)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))
        # One subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('is_tree_symmetric.py',
																																	'is_tree_symmetric.tsv', is_symmetric))

