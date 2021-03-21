# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have
# the same value.
#
# Example 1:
# Input: p = [1, 2, 3], q = [1, 2, 3]
# Output: true
#
# Example 2:
# Input: p = [1, 2], q = [1, null, 2]
# Output: false
#
# Example 3:
# Input: p = [1, 2, 1], q = [1, 1, 2]
# Output: false
#
# Constraints:
#
# The number of nodes in both trees is in the range[0, 100].
# -104 <= Node.val <= 104

from BinaryTrees import binary_tree


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


a = binary_tree([])
b = binary_tree([])
assert is_same_tree(a, b) is True

a = binary_tree([])
b = binary_tree([1])
assert is_same_tree(a, b) is False

a = binary_tree([1])
b = binary_tree([])
assert is_same_tree(a, b) is False

a = binary_tree([1])
b = binary_tree([1])
assert is_same_tree(a, b) is True

a = binary_tree([1])
b = binary_tree([2])
assert is_same_tree(a, b) is False

a = binary_tree([1, 2])
b = binary_tree([1])
assert is_same_tree(a, b) is False

a = binary_tree([1])
b = binary_tree([1, 2])
assert is_same_tree(a, b) is False

a = binary_tree([1, 2, 3])
b = binary_tree([1, 2, 3])
assert is_same_tree(a, b) is True

a = binary_tree([1, 2, 3])
b = binary_tree([1, 3, 2])
assert is_same_tree(a, b) is False
