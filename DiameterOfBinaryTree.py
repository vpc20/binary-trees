# Diameter of Binary Tree
#
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary
# tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through
# the root.
#
# Example:
# Given a binary tree
#
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# def diameter(node):
#     """
#     The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
#     This path may or may not pass through the root.
#
#     :param node: node of the tree
#     :return: diameter of the tree
#     """
#
#     def dfs(curr):
#         nonlocal maxval
#         if curr.left is None and curr.right is None:
#             return 0
#         left = 0
#         right = 0
#         if curr.left:
#             left = 1 + dfs(curr.left)
#         if curr.right:
#             right = 1 + dfs(curr.right)
#         maxval = max(maxval, left + right)
#         return max(left, right)
#
#     if node is None:
#         return 0
#     maxval = 0
#     dfs(node)
#     return maxval


# def diameter(node):
#     def traverse(curr):
#         hleft = 0
#         hright = 0
#         if curr.left:
#             hleft = height(curr.left) + 1
#             traverse(curr.left)
#         if curr.right:
#             hright = height(curr.right) + 1
#             traverse(curr.right)
#         harr.append(hleft + hright)
#
#     if node is None:
#         return 0
#     harr = []
#     traverse(node)
#     return max(harr)
from BinaryTrees import binary_tree


def diameter(node):
    def height(node):
        nonlocal maxd
        left = right = 0
        if node.left:
            left = 1 + height(node.left)
        if node.right:
            right = 1 + height(node.right)
        maxd = max(maxd, left + right)
        return max(left, right)

    maxd = 0
    height(node)
    return maxd


# def diameterOfBinaryTree(self, root):
#     self.ans = 1
#
#     def depth(node):
#         if not node: return 0
#         L = depth(node.left)
#         R = depth(node.right)
#         self.ans = max(self.ans, L + R + 1)
#         return max(L, R) + 1
#
#     depth(root)
#     return self.ans - 1

if __name__ == '__main__':
    t = binary_tree([1, 2, 3, 4, 5])
    assert diameter(t) == 3
