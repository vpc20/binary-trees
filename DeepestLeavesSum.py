# Given the root of a binary tree, return the sum of values of its deepest leaves.
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]
# Output: 15
#
# Example 2:
# Input: root = [6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5]
# Output: 19
#
# Constraints:
# The number of nodes in the tree is in the range[1, 104].
# 1 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

from BinaryTreeLevelOrderTraversal import level_order
from BinaryTrees import binary_tree


def deepest_leaves_sum(root):
    q = deque([root])
    while q:
        lsum = 0
        for _ in range(len(q)):
            node = q.popleft()
            lsum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return lsum


# arr = [3, 9, 20, None, None, 15, 7]
arr = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]
t = binary_tree(arr)
print(t)
print(level_order(t))
print(deepest_leaves_sum(t))
