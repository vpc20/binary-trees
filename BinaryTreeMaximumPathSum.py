# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in
# the tree along the parent-child connections. The path must contain at least one node and does not need
# to go through the root.
#
# Example 1:
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
#
# Example 2:
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42

# Definition for a binary tree node.
import sys
# from collections import deque


# def find_max_util(root):
#     if root is None:
#         return 0
#
#     l = find_max_util(root.left)
#     r = find_max_util(root.right)
#
#     max_single = max(max(l, r) + root.val, root.val)
#     max_top = max(max_single, l + r + root.val)
#
#     find_max_util.res = max(find_max_util.res, max_top)
#     return max_single
from BinaryTrees import binary_tree


def max_path_sum(root):
    def find_max(root):
        nonlocal maxsum
        if root is None:
            return 0

        maxl = find_max(root.left)
        maxr = find_max(root.right)

        max_root = max(maxl + root.val, maxr + root.val, root.val)
        maxsum = max(maxsum, max_root, maxl + maxr + root.val)
        return max_root

    maxsum = -sys.maxsize
    find_max(root)
    return maxsum


t = binary_tree([-10, 9, 20, None, None, 15, 7])
print(t)
print(max_path_sum(t))
