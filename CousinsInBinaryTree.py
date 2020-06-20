# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in
# the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
# Note:
#
#     The number of nodes in the tree will be between 2 and 100.
#     Each node has a unique integer value from 1 to 100.
from BinaryTrees import binary_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def is_cousins(root, x, y):
#     def is_cousins_aux(curr, parent, depth):
#         nonlocal depthx, depthy, parentx, parenty
#         if curr is None:
#             return
#         if curr.val == x:
#             depthx = depth
#             parentx = parent
#         if curr.val == y:
#             depthy = depth
#             parenty = parent
#         is_cousins_aux(curr.left, curr, depth + 1)
#         is_cousins_aux(curr.right, curr, depth + 1)
#
#     depthx, depthy, parentx, parenty = 0, 0, None, None
#     is_cousins_aux(root, root, 0)
#     return depthx == depthy and parentx != parenty

def is_cousins(root, x, y):
    def is_cousins_aux(curr, parent, depth):
        nonlocal depthx, depthy, parentx, parenty
        if curr.val == x:
            depthx = depth
            parentx = parent
        if curr.val == y:
            depthy = depth
            parenty = parent
        if curr.left:
            is_cousins_aux(curr.left, curr, depth + 1)
        if curr.right:
            is_cousins_aux(curr.right, curr, depth + 1)

    depthx, depthy, parentx, parenty = 0, 0, None, None
    is_cousins_aux(root, root, 0)
    return depthx == depthy and parentx != parenty


def depth(root, x):
    def dfs(curr, depth):
        nonlocal depthx
        if curr.val == x:
            depthx = depth
        if curr.left:
            dfs(curr.left, depth + 1)
        if curr.right:
            dfs(curr.right, depth + 1)

    depthx = 0
    dfs(root, 0)
    return depthx


arr = [1, 2, 3, None, 4, None, 5]
t = binary_tree(arr)
print(t)
assert is_cousins(t, 5, 4) is True
assert is_cousins(t, 2, 3) is False
assert is_cousins(t, 4, 5) is True

assert depth(t, 1) == 0
assert depth(t, 2) == 1
assert depth(t, 3) == 1
assert depth(t, 4) == 2
assert depth(t, 5) == 2
