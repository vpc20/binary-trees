# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]
#
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
from BinaryTrees import TreeNode, print_preorder, print_inorder, print_level_order, print_postorder

# preorder[4, 2, 1, 3, 6, 5, 7]
# inorder [1, 2, 3, 4, 5, 6, 7]


def build_tree(preorder, inorder):
    if not inorder:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    root = TreeNode(preorder[0])
    i = inorder.index(preorder[0])  # root index for inorder
    root.left = build_tree(preorder[1:i + 1], inorder[:i])
    root.right = build_tree(preorder[i + 1:], inorder[i + 1:])
    return root


# def build_tree(preorder, inorder):
#     print(preorder, inorder)
#     if len(inorder) == 1:
#         return TreeNode(preorder[0])
#     root = TreeNode(preorder[0])
#     i = inorder.index(preorder[0])
#     j = preorder.index(inorder[0])
#     root.left = build_tree(preorder[:j], inorder[:i])
#     root.right = build_tree(preorder[j + 1:], inorder[i + 1:])
#     # left_idx = preorder.index(inorder[0])
#     # root_idx = inorder.index(preorder[0])
#     # root.left = build_tree(preorder[left_idx:], inorder[:root_idx])
#     # root.right = build_tree(preorder[left_idx + 1], inorder[root_idx + 1:])
#     return root

print(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
print(build_tree([4, 2, 1, 3, 6, 5, 7], [1, 2, 3, 4, 5, 6, 7]))
