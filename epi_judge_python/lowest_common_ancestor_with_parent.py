import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# reimplemntation of the book answer
# 1/7/21
# 9.4
def lca(node0, node1):
	def depth(node):
		ret = 0
		while node:
			ret += 1
			node = node.parent
		return ret
	
	depth0, depth1 = map(depth, (node0, node1))
	if depth1 > depth0: # force node 0 to be the deeper node
		node0, node1 = node1, node0
		
	delta = abs(depth1 - depth0)
	for i in range(delta):
		node0 = node0.parent
	
	while node0 != node1:
		node0, node1 = node0.parent, node1.parent
	return node0	



def lca_book(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node):
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    depth0, depth1 = map(get_depth, (node0, node1))
    # Makes node0 as the deeper node in order to simplify the code.
    if depth1 > depth0:
        node0, node1 = node1, node0

    # Ascends from the deeper node.
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        node0 = node0.parent
        depth_diff -= 1

    # Now ascends both nodes until we reach the LCA.
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0


# below is my failed attempt. It failed because namedtuples are immutable lmao
from collections import  namedtuple
def my_failed_lca(node0: BinaryTreeNode,
								node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
	nodeAndPath = namedtuple("nodeAndPath",("n","path"))
	n0 = nodeAndPath(node0, set())
	n1 = nodeAndPath(node1, set())
	
	def check_and_advance(advancing, static):
		if advancing.n in static.path:
			print("is")
			ret = advancing.n
			advancing.n = None
			static.n = None
			return ret
		else:
			print("else")
			advancing.path.add(advancing.n)
			print("next")
			advancing.n = advancing.n.parent			
			print("done")
		
		
	while n0.n and n1.n:
		print("iter")
		if n0.n:
			print("n0")
			r = check_and_advance(n0,n1)
			if r:
				return r
		if n1.n:
			print("n1")
			r = check_and_advance(n1,n0)
			if r:
				return r
			
	return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
	result = executor.run(
		functools.partial(lca,
																				must_find_node(tree, node0), must_find_node(tree, node1)))

	if result is None:
		raise TestFailure('Result can\'t be None')
	return result.data


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
																																	'lowest_common_ancestor.tsv', lca_wrapper))
	
