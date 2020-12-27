from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 8.6
# each node's distance from root is its depth.
# given binary tree, return array consisting of keys at the same level.
# keys sould appear in order of nodes' depths. break ties left to right.

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
