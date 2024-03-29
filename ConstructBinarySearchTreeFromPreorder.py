# Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches the given preorder traversal.
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a
# value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then traverses node.right.)
#
# Example 1:
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
#                   8
#              5          10
#          1      7   null   12
# Note:
#     1 <= preorder.length <= 100
#     The values of preorder are distinct.

from BinaryTrees import TreeNode


# def insert(curr, v):
#     if v < curr.val:
#         if curr.left is None:
#             curr.left = TreeNode(v)
#             return
#         insert(curr.left, v)
#     else:
#         if curr.right is None:
#             curr.right = TreeNode(v)
#             return
#         insert(curr.right, v)


def insert(curr, v):
    while True:
        if v < curr.val:
            if curr.left is None:
                curr.left = TreeNode(v)
                return
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = TreeNode(v)
                return
            curr = curr.right


# def bst_from_preorder(preorder):
#     root = TreeNode(preorder[0])
#     for e in preorder[1:]:
#         insert(root, e)
#     return root


def bst_from_preorder(preorder):
    root = TreeNode(preorder[0])
    for i in range(1, len(preorder)):
        insert(root, preorder[i])
    return root


def bst_from_preorder1(preorder):
    if not preorder:
        return None

    node = TreeNode(preorder[0])
    if len(preorder) == 1:
        return node

    i = 0
    for i in range(1, len(preorder)):
        if preorder[i] > preorder[0]:
            break
    if preorder[0] > preorder[-1]:
        i += 1

    node.left = bst_from_preorder1(preorder[1:i])
    node.right = bst_from_preorder1(preorder[i:])

    return node


# preorder = [8, 5, 1, 7, 10, 12]
preorder = [4, 2, 1, 3, 6, 5, 7]
# preorder = [4, 2, 1]
# preorder = [4]

t = bst_from_preorder(preorder)
print(t)

t1 = bst_from_preorder1(preorder)
print(t1)
