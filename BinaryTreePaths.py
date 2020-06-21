# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

from BinaryTrees import binary_tree


# def binary_tree_paths(node):
#     def dfs(node, path):
#         if node.left is None and node.right is None:
#             paths.append(path)
#         if node.left:
#             dfs(node.left, path + [node.left.val])
#         if node.right:
#             dfs(node.right, path + [node.right.val])
#
#     if node is None:
#         return 0
#     paths = []
#     dfs(node, [node.val])
#     return paths


def binary_tree_paths(node):
    def dfs(node, path):
        if node.left is None and node.right is None:
            paths.append(path)
        if node.left:
            dfs(node.left, f'{path}->{node.left.val}')
        if node.right:
            dfs(node.right, f'{path}->{node.right.val}')

    if node is None:
        return []
    paths = []
    dfs(node, str(node.val))
    return paths


t = binary_tree([1, 2, 3, 4, 5, 6, 7])
print(t)
print(binary_tree_paths(t))
