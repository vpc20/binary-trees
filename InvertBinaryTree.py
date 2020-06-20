# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
from BinaryTrees import binary_tree


def invert_tree(root):
    if root is None:
        return root
    if root.left:
        invert_tree(root.left)
    if root.right:
        invert_tree(root.right)
    root.left, root.right = root.right, root.left
    return root


t = binary_tree([4, 2, 7, 1, 3, 6, 9])
print(t)
print(invert_tree(t))
