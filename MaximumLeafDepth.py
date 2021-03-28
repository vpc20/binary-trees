from BinaryTrees import binary_tree


# def max_leaf_depth(root):
#     def preorder(node, lvl):
#         nonlocal maxlvl
#         if node.left is None and node.right is None:
#             maxlvl = max(maxlvl, lvl)
#             return
#         if node.left is not None:
#             preorder(node.left, lvl + 1)
#         if node.right is not None:
#             preorder(node.right, lvl + 1)
#
#     if root is None:
#         return 0
#     maxlvl = 0
#     preorder(root, 0)
#     return maxlvl


def max_leaf_depth(root):
    if root is None:
        return 0
    left = right = 0
    if root.left:
        left = 1 + max_leaf_depth(root.left)
    if root.right:
        right = 1 + max_leaf_depth(root.right)
    return max(left, right)


if __name__ == '__main__':
    t = binary_tree([3, 9, 20, None, None, 15, 7])
    print(t)
    print(max_leaf_depth(t))

    t = binary_tree([1])
    print(t)
    print(max_leaf_depth(t))
