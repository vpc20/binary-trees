# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string
# is a valid sequence in such binary tree.
#
# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of
# the nodes along a path results in a sequence in the given binary tree.

# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation:
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
# Other valid sequences are:
# 0 -> 1 -> 1 -> 0
# 0 -> 0 -> 0
from BinaryTrees import binary_tree


# def is_valid_sequence(root, arr):
#     def dfs(curr, seq):
#         nonlocal result
#         if curr.left is None and curr.right is None:  # is a leaf
#             if seq == arr:
#                 result = True
#         if curr.left:
#             dfs(curr.left, seq + [curr.left.val])
#         if curr.right:
#             dfs(curr.right, seq + [curr.right.val])
#
#     result = False
#     dfs(root, [root.val])
#     return result


def is_valid_sequence(root, arr):
    def dfs(curr, seq):
        if curr.left is None and curr.right is None:  # is a leaf
            if seq == arr:
                return True
        if curr.left:
            if dfs(curr.left, seq + [curr.left.val]):
                return True
        if curr.right:
            if dfs(curr.right, seq + [curr.right.val]):
                return True
        return False

    return dfs(root, [root.val])


# def is_valid_sequence(root, arr):
#     def dfs(curr, seq):
#         if curr.left is None and curr.right is None:  # is a leaf
#             if seq == arr:
#                 return True
#         if curr.left:
#             if dfs(curr.left, seq + [curr.left.val]):
#                 return True
#         if curr.right:
#             if dfs(curr.right, seq + [curr.right.val]):
#                 return True
#         return False
#
#     return dfs(root, [root.val])


t = binary_tree([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0])
assert is_valid_sequence(t, [0, 1, 0, 1]) is True
assert is_valid_sequence(t, [0, 1, 1, 0]) is True
assert is_valid_sequence(t, [0, 0, 0]) is True
assert is_valid_sequence(t, [0]) is False
assert is_valid_sequence(t, [1]) is False
assert is_valid_sequence(t, [0, 1, 1, 1]) is False
